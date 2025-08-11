from pydantic import BaseModel, EmailStr

class SavedVerse(BaseModel):
    username: str
    verse: str 
    feeling: str | None = None

    class Config:
        orm_mode = True     #This is what enables the conversion from SQLAlchemy to Pydantic conversion
        
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    username: str
    emial: EmailStr

    class Config:
        orm_mode = True