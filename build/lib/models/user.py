from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.base import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)

    entries = relationship("Entry", back_populates="user")
    meal_plans = relationship("MealPlan", back_populates="user")
