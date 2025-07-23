from fastapi import APIRouter, HTTPException
from application.chat.handlers import ChatApplicationService

router = APIRouter()
chat_service = ChatApplicationService()

@router.post("/")
async def talk_to_character(character: str, message: str, session_id: str):
    try:
        response = await chat_service.handle_chat(session_id, character, message)
        return {"response": response}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))