from sqlalchemy import Column, Integer, String, ForeignKey
from app.db import Base

class TestCase(Base):
    __tablename__ = "testcases"  # This must match the actual table name in DB

    id = Column(Integer, primary_key=True, index=True)
    problem_id = Column(Integer, ForeignKey("problems.id"), nullable=False)
    input = Column(String, nullable=False)
    output = Column(String, nullable=False)