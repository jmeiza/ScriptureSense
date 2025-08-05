from sqlalchemy import Column, Integer, String
from ..database import Base

class SavedVerse(Base):
    __tablename__ = "saved_verses"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True)
    verse = Column(String)
    feeling = Column(String, nullable=True)
    
