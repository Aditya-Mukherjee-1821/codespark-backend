from app.database import engine  # This is the async engine
from app.models import problem  # This triggers model registration
from app.db import Base
import asyncio

async def init_models():
    async with engine.begin() as conn:
        from app.models import problem
        await conn.run_sync(Base.metadata.create_all)

if __name__ == "__main__":
    asyncio.run(init_models())
