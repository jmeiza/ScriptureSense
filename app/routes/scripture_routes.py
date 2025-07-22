from fastapi import APIRouter
from services.scripture_service import get_Scripture_for_feeling

router = APIRouter()

@router.post("/get-scripture")
def get_scripture(feeling: str):
    verse = get_Scripture_for_feeling(feeling)
    return {"feeling": feeling, "verse":verse}