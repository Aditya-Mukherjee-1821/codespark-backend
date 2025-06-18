from fastapi import FastAPI
from .routers import problems, submissions, feedback
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["http://localhost:3001"] 

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ⚠️ For local testing only
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(problems.router, prefix="/problems", tags=["Problems"])
app.include_router(submissions.router, prefix="/submissions", tags=["Submissions"])
app.include_router(feedback.router)  

import asyncio
from keep_alive import ping_db

@app.on_event("startup")
async def startup_event():
    asyncio.create_task(ping_db())