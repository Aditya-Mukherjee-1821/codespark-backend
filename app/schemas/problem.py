from pydantic import BaseModel
from typing import List, Optional, Dict

class ProblemOut(BaseModel):
    id: int
    title: str
    description: str
    difficulty: str
    rating: int
    examples: Optional[List[Dict]]

    class Config:
        orm_mode = True
