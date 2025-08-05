from fastapi import APIRouter, Query, HTTPException
from ..services.openai_service import find_top_verses

router = APIRouter()

@router.get("/get-scripture")
def get_scripture(feeling: str = Query(default=None, min_length=3, max_length=100)):
    feeling = feeling.strip()
    if not feeling:
        raise HTTPException(status_code=400, detail="Feeling cannot be empty.")
    
    results = find_top_verses(feeling)
    
    if results:
        return {"feeling": feeling, "matches": results}
    else:
        raise HTTPException(status_code=400, detail="No matching scripture found.")

