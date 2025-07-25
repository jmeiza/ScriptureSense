import json
from fastapi import APIRouter
from ..models.schema import SavedVerse
from pathlib import Path

router = APIRouter()

SAVE_PATH = Path("data/saved_verses.json")

def load_all():
    if not SAVE_PATH.exists():          # If the file doesn't exists yet, create it
        SAVE_PATH.parent.mkdir(parents=True, exist_ok=True)
        with open(SAVE_PATH, "w") as f:
            json.dump({}, f, indent=4)
        return {}
    
    with open(SAVE_PATH, "r") as f:
        return json.load(f)

def save_all(data):
    with open(SAVE_PATH, "w") as f:
        json.dump(data, f, indent=4)

@router.post("/save-verse")
def save_verse(saved_verse: SavedVerse):
    data = load_all()
    user_verses = data.setdefault(saved_verse.username, [])
    user_verses.append(saved_verse.dict())
    save_all(data)
    return {"message": "Verse saved successfully."}

@router.get("/get-saved/{username}")
def get_saved_verses(username: str):
    data = load_all()
    return data.get(username, [])