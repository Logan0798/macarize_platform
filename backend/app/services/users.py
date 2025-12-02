from sqlalchemy.orm import Session
from app.models.users import User
from app.schemas.users import UserCreate
from app.core.security import hash_password
import uuid


def create_user(db: Session, data: UserCreate) -> User:
    user = User(
        id=uuid.uuid4(),
        email=data.email,
        first_name=data.first_name,
        last_name=data.last_name,
        password_hash=hash_password(data.password),
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
