from fastapi import APIRouter
from ..services.scripture_service import get_scripture_for_feeling

router = APIRouter()

@router.get("/get-scripture")
def get_scripture(feeling: str):
    verses_by_theme = get_scripture_for_feeling(feeling)
    
    return {"feeling": feeling, "verse":verses_by_theme}