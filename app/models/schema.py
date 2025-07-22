from pydantic import BaseModel

class SavedVerse(BaseModel):
    username: str 
    feeling: str
    verse: str