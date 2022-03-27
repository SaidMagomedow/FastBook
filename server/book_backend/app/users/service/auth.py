from typing import Optional

from app.database import SessionLocal
from users.models.user_models import User

from .security import verify_password


def authenticate(username: str, password: str, db: SessionLocal) -> Optional[User]:
    user = db.query(User).filter(User.username == username).first()
    if not user:
        return None
    if not verify_password(password, user.hashed_password):
        return None
    return user
