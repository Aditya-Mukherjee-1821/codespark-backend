# app/db/session.py
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import declarative_base
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")  # should be like: postgresql+asyncpg://user:pass@localhost:5433/dbname

# Async engine
engine = create_async_engine(DATABASE_URL, echo=True)

# Async session maker
AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    expire_on_commit=False,
    class_=AsyncSession
)

# Dependency
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session

Base = declarative_base()
