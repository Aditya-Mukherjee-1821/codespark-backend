import asyncio
import asyncpg
import os

async def ping_db():
    db_url = os.getenv("DATABASE_URL")
    while True:
        try:
            conn = await asyncpg.connect(db_url)
            await conn.execute("SELECT 1;")
            await conn.close()
            print("Pinged DB successfully.")
        except Exception as e:
            print("DB ping failed:", e)
        await asyncio.sleep(50)

if __name__ == "__main__":
    asyncio.run(ping_db())
