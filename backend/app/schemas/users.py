from pydantic import BaseModel, EmailStr
from typing import Optional
from uuid import UUID
from datetime import datetime


# Returned to clients
class UserRead(BaseModel):
    id: UUID
    email: EmailStr
    first_name: str
    last_name: str
    is_active: bool
    is_superuser: bool
    auth_provider: str
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True  # allows sqlalchemy models -> pydantic conversion


# Data required to create a new user
class UserCreate(BaseModel):
    email: EmailStr
    first_name: str
    last_name: str
    password: str


# Data allowed to update a user
class UserUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    is_active: Optional[bool] = None
    is_superuser: Optional[bool] = None
