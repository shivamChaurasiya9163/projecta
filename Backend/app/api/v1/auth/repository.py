from sqlalchemy.orm import Session

from app.models.user import User


class UserRepository:

    @staticmethod
    def get_by_email(
        db: Session,
        email: str
    ):

        return (
            db.query(User)
            .filter(User.email == email)
            .first()
        )

    @staticmethod
    def create(
        db: Session,
        user: User
    ):

        try:

            db.add(user)

            db.commit()

            db.refresh(user)

            return {
                "success": True,
                "message": "User Registered Successfully",
                "data": {
                    "id": user.id,
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                    "email": user.email,
                    "phone": user.phone
                }
            }

        except Exception as e:

            db.rollback()

            raise e