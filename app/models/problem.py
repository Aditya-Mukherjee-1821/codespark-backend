from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.dialects.postgresql import JSONB
from app.db import Base  # This is now valid

class Problem(Base):
    __tablename__ = "problems"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    difficulty = Column(String, nullable=False)
    rating = Column(Integer, nullable=False)
    description = Column(Text, nullable=True)
    examples = Column(JSONB, nullable=True)
