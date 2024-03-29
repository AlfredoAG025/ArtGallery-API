from sqlalchemy.orm import Session

from schemas.user import UserCreate
from db.models.user import User
from core.hashing import Hasher


def create_new_user(user: UserCreate, db: Session):
    user = User(
        username=user.username,
        email=user.email,
        password=Hasher.get_password_hashed(user.password),
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
