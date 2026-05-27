from fastapi import APIRouter
from pydantic import BaseModel

from app.core.orchestrator import EireneOrchestrator


router = APIRouter()

eirene = EireneOrchestrator()


class ChatRequest(BaseModel):

    message: str


@router.post("/chat")

def chat(request: ChatRequest):

    result = eirene.process_user_message(
        request.message
    )

    return result
