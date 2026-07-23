from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    """
    Incoming request from the website chatbot.
    """

    message: str = Field(
        ...,
        min_length=1,
        max_length=2000,
        description="User's message"
    )


class ChatResponse(BaseModel):
    """
    Response returned to the frontend.
    """

    reply: str


class ErrorResponse(BaseModel):
    """
    Error response.
    """

    error: str