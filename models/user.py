from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database.setup import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)

    entries = relationship("Entry", back_populates="user")
    goals = relationship("Goal", back_populates="user")
