from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..models.schema import SavedVerse as SavedVerseSchema
from ..models.saved_verse_model import SavedVerse
from ..models.database import get_db

router = APIRouter()

@router.post("/save-verse")
def save_verse(saved_verse: SavedVerseSchema, db: Session = Depends(get_db)):
    verse = SavedVerse(**saved_verse.dict())
    db.add(verse)
    db.commit()
    db.refresh(verse)
    return {"message": "Verse saved successfully.", "id": verse.id}

@router.get("/get-saved/{username}", response_model=List[SavedVerseSchema])
def get_saved_verses(username: str, db: Session = Depends(get_db)):
    return db.query(SavedVerse).filter(SavedVerse.username == username).all()
    