from pydantic import BaseModel, EmailStr
from datetime import datetime


class UserResponse(BaseModel):

    id: int

    first_name: str

    last_name: str

    email: EmailStr

    phone: str

    is_active: bool

    is_verified: bool

    created_at: datetime

    class Config:
        from_attributes = True