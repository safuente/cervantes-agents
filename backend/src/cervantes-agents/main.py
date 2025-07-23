from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from interface.api.chat import router as chat_router

app = FastAPI(title="Cervantes Agents")

app.include_router(chat_router, prefix="/api/chat", tags=["Chat"])