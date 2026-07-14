from sqlalchemy.orm import Session

from app.schemas.auth import SignupRequest
from app.api.v1.auth.service import AuthService


class AuthController:

    @staticmethod
    def signup(
        request: SignupRequest,
        db: Session
    ):
        return AuthService.signup(
            db,
            request
        )