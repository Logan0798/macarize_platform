from pydantic import BaseModel, EmailStr
from typing import Optional
from uuid import UUID
from datetime import datetime


class InvitationRead(BaseModel):
    id: UUID
    email: EmailStr
    invited_by: Optional[UUID] = None
    token: str
    expires_at: datetime
    accepted_at: Optional[datetime] = None
    created_at: datetime

    class Config:
        from_attributes = True


class InvitationCreate(BaseModel):
    email: EmailStr
    invited_by: Optional[UUID] = None


class InvitationAccept(BaseModel):
    token: str
