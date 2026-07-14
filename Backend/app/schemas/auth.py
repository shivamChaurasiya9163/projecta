from pydantic import BaseModel, EmailStr, Field


class SignupRequest(BaseModel):

    first_name: str = Field(..., min_length=2, max_length=100)

    last_name: str = Field(..., min_length=2, max_length=100)

    email: EmailStr

    phone: str

    password: str = Field(..., min_length=8)

    #confirm_password: str


class LoginRequest(BaseModel):

    email: EmailStr

    password: str


class TokenResponse(BaseModel):

    access_token: str

    refresh_token: str

    token_type: str = "Bearer"