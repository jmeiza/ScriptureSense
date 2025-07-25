from fastapi import APIRouter, Query, HTTPException
from ..services.scripture_service import get_scripture_for_feeling, get_verse_by_theme

router = APIRouter()

@router.get("/get-scripture")
def get_scripture(feeling: str = Query(default=None, min_length=3, max_length=100), theme: str = Query(default=None, min_length=3, max_length=100)):

    if theme:
        theme = theme.strip()
        if not theme:
            raise HTTPException(status_code=400, detail="Theme cannot be empty.")
        verse = get_verse_by_theme(theme)
        return {"theme": theme, " verse":verse}

    if feeling:
        feeling = feeling.strip()
        if not feeling:
            raise HTTPException(status_code=400, detail="Feeling cannot be empty.")
        verse = get_scripture_for_feeling(feeling)
        return {"feeling":feeling, **verse}
    
    raise HTTPException(status_code=400, detail="You must provide either a 'feeling' or a 'theme'.")

# **response is called dictionary unpacking