from sqlalchemy import Column, Integer, String, ForeignKey
from models.base import Base

class Goal(Base):
    __tablename__ = "goals"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    name = Column(String, nullable=False)
    daily = Column(Integer, nullable=True)
    weekly = Column(Integer, nullable=True)
