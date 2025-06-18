from sqlalchemy.orm import Session
from app.models.problem import Problem
from app.models.testcase import TestCase

def get_all_problems(db: Session):
    return db.query(Problem).all()

def get_problem(db: Session, problem_id: int):
    return db.query(Problem).filter(Problem.id == problem_id).first()

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.testcase import TestCase

async def get_problem_by_id(db: AsyncSession, problem_id: int):
    result = await db.execute(select(Problem).where(Problem.id == problem_id))
    return result.scalars().first()
