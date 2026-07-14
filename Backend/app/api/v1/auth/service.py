from app.models.user import User
from app.api.v1.auth.repository import UserRepository


class AuthService:

    @staticmethod
    def signup(
        db,
        request
    ):

        existing = UserRepository.get_by_email(
            db,
            request.email
        )

        if existing:
            raise Exception("Email already exists")

        user = User(
            first_name=request.first_name,
            last_name=request.last_name,
            email=request.email,
            phone=request.phone,
            password=request.password
        )

        return UserRepository.create(
            db,
            user
        )