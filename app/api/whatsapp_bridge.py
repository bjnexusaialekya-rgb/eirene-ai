from fastapi import APIRouter
from pydantic import BaseModel

from app.core.orchestrator import CognitiveOrchestrator

router = APIRouter()

orchestrator = CognitiveOrchestrator()

class WhatsAppMessage(BaseModel):

    message: str

    sender: str = "whatsapp_user"

@router.post("/whatsapp")

async def whatsapp_chat(data: WhatsAppMessage):

    response = orchestrator.process_message(

        user_id=data.sender,

        message=data.message

    )

    return {

        "reply": response
    }
