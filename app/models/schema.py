from pydantic import BaseModel, EmailStr

# Saved Verse Schemas
class SavedVerseBase(BaseModel):
    verse: str 
    reference: str
    feeling: str | None = None

    class Config:
        from_attributes = True     #This is what enables the conversion from SQLAlchemy to Pydantic conversion

class SavedVerseCreate(SavedVerseBase):
    pass

class SavedVerseResponse(SavedVerseBase):
    id: int
    user_id: int

    class Config:
        from_attributes = True


# User schemas
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
    email: EmailStr

    class Config:
        orm_mode = True