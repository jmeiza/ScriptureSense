from fastapi import APIRouter
from ..models.schema import SavedVerse

router = APIRouter()

saved_verses_store = {}

@router.post("/save-verse")
def save_verse(saved_verse: SavedVerse):
    user_verses = saved_verses_store.setdefault(saved_verse.username, [])
    user_verses.append(saved_verse)
    return {"message": "Verse saved successfully."}

@router.get("/get-saved/{username}")
def get_saved_verses(username: str):
    return saved_verses_store.get(username, [])