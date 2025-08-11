from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..models.schema import SavedVerseCreate, SavedVerseResponse
from ..models.saved_verse_model import SavedVerse
from ..models.database import get_db
from ..services.utils import get_current_user

router = APIRouter(tags=["Saved Verses"])

@router.post("/", response_model=SavedVerseResponse)
def save_verse(saved_verse: SavedVerseCreate, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):

    verse = SavedVerse(**saved_verse.dict(), user_id=current_user["user_id"])
    db.add(verse)
    db.commit()
    db.refresh(verse)
    return verse

@router.get("/", response_model=List[SavedVerseResponse])
def get_saved_verses(db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    verses = db.query(SavedVerse).filter(SavedVerse.user_id == current_user["user_id"]).all()
    return verses
    