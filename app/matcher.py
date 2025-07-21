import json
import random

# Load scripture data
with open("data/scriptures.json","r") as f:
    scripture_data = json.load(f)

# Simple keyword-to-theme mapping
keywords_map = {
    "anxious": "anxiety",
    "worried": "anxiety",
    "grieving": "grief",
    "sad": "grief",
    "afraid": "fear",
    "scared": "fear",
    "happy": "happy",
}

def get_scripture_for_feeling(feeling_input: str):
    for word, theme in keywords_map.items():
        if word in feeling_input.lower():
            return random.choice(scripture_data.get(theme, ["No verse found."]))
        
    return "Sorry, we couldn't find a verse for that feeling."