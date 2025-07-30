from pydantic import BaseModel

class SavedVerse(BaseModel):
    username: str
    verse: str 
    theme: str | None = None
    feeling: str | None = None

    class Config:
        orm_mode = True     #This is what enables the conversion from SQLAlchemy to Pydantic conversion
        
    