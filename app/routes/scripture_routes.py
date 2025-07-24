from fastapi import APIRouter
from ..services.scripture_service import get_scripture_for_feeling

router = APIRouter()

@router.get("/get-scripture")
def get_scripture(feeling: str):
    verses = get_scripture_for_feeling(feeling)
    
    if not verses:
        return {"feeling": feeling, "message": "No matching verses found for that feeling."}
    
    return {"feeling": feeling, "verse":verses}