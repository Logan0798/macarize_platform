from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.users import UserCreate, UserRead
from app.services.users import create_user
from app.core.db import get_db

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/", response_model=UserRead)
def create_new_user(data: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, data)
