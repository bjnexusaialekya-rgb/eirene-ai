from fastapi import APIRouter

from app.schemas.chat_schema import ChatRequest
from app.core.orchestrator import EireneOrchestrator


router = APIRouter()

eirene = EireneOrchestrator()


@router.post("/chat")
def chat(request: ChatRequest):

    result = eirene.process_message(
        request.message
    )

    return result