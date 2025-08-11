from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class SavedVerse(Base):
    __tablename__ = "saved_verses"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    verse = Column(String, nullable=False)
    reference = Column(String, nullable=False)
    feeling = Column(String, nullable=True)

    user = relationship("User", back_populates="saved_verses")
    
