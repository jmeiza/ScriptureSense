from pydantic import BaseModel

class SavedVerse(BaseModel):
    username: str
    verse: str 
    feeling: str | None = None

    class Config:
        orm_mode = True     #This is what enables the conversion from SQLAlchemy to Pydantic conversion
        
    