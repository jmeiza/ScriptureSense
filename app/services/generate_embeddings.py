import os
import json
from dotenv import load_dotenv
from openai import OpenAI
from pathlib import Path

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)


BASE_DIR = Path(__file__).resolve().parent
scriptures_path = BASE_DIR / ".." / "data" / "scriptures.json"
embeddings_output_path = BASE_DIR / "verse_embeddings.json"

with open(scriptures_path, "r", encoding="utf-8") as f:
    scriptures = json.load(f)

# Load existing emebeddings if there any
try:
    with open(embeddings_output_path, "r", encoding="utf-8") as f:
        existing_embeddings = json.load(f)
except FileNotFoundError:
    existing_embeddings = []

embedded_ids = {e["id"] for e in existing_embeddings}

embeddings = existing_embeddings.copy()

for verse in scriptures:
    if verse["id"] in embedded_ids:
        print(f"Skipping verse if {verse['id']} (already embedded).")
        continue

    text = verse["text"]
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=text
    )
    embedding = response.data[0].embedding
    embeddings.append({
        "id": verse["id"],
        "embedding": embedding
    })
    print(f"Embedded verse id {verse['id']}.")

# Save updated embeddings
with open(embeddings_output_path, "w", encoding="utf-8") as f:
    json.dump(embeddings, f)

print(f"Total embeddings saved: {len(embeddings)}")