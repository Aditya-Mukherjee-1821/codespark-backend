from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.database import SessionLocal
from app.models.problem import Problem
from app.schemas.problem import ProblemOut

router = APIRouter()

async def get_db():
    async with SessionLocal() as session:
        yield session

@router.get("/", response_model=list[ProblemOut])
async def get_problems(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Problem))
    return result.scalars().all()

@router.get("/{problem_id}", response_model=ProblemOut)
async def get_problem(problem_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Problem).where(Problem.id == problem_id))
    problem = result.scalar_one_or_none()
    if not problem:
        raise HTTPException(status_code=404, detail="Problem not found")
    return problem
