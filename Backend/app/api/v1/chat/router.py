from fastapi import APIRouter, HTTPException

from .schemas import ChatRequest, ChatResponse
from .service import generate_reply

router = APIRouter()


@router.post(
    "/",
    response_model=ChatResponse,
    summary="Chat with SGenovix AI"
)
async def chatbot(request: ChatRequest):
    """
    Receives a message from the frontend chatbot
    and returns an AI-generated response.
    """

    try:

        reply = generate_reply(request.message)

        return ChatResponse(
            reply=reply
        )

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=f"Chatbot Error: {str(e)}"
        )