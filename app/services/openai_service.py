import os
import json
import numpy as np
from openai import OpenAI
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
scriptures_path = BASE_DIR / ".." / "data" / "scriptures.json"
embeddings_path = BASE_DIR / "verse_embeddings.json"

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("Missing OPENAI_API_KEY in environment variables.")

client = OpenAI(api_key=api_key)

# Load scriptures and embeddings 
with open(scriptures_path, "r", encoding="utf-8") as f:
    scriptures = json.load(f)

with open(embeddings_path, "r", encoding="utf-8") as f:
    verse_embeddings = json.load(f)


# This function is used to measure how aligned (similar) two vectors are.
# One vector represents a verse and the other represents the user's input
def cosine_similarity(vec1, vec2):
    vec1 = np.array(vec1)
    vec2 = np.array(vec2)
    
    if np.linalg.norm(vec1) == 0 or np.linalg.norm(vec2) == 0:
        return 0

    return np.dot(vec1,vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))

# Generate embeddings for the textit is given. Embeddiings are like number (vector) representations of text
def generate_embedding(text: str):
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=text
    )
    return response.data[0].embedding

# This function gets the cosine similarity between the user input and all the verse embeddings and returns the top 3
def find_top_verses(user_input: str, top_n: int = 3):
    input_embedding = generate_embedding(user_input)
    scores = []
    for ve in verse_embeddings:
        score = cosine_similarity(input_embedding, ve["embedding"])
        scores.append((score, ve["id"]))
    
    scores.sort(key=lambda x: x[0], reverse=True)
    top_matches = scores[:top_n]

    results = []
    for score, vid in top_matches:
        verse = next((v for v in scriptures if v["id"] == vid), None)
        if verse:
            results.append({
                "score": score,
                "verse": verse
            })
    return results
