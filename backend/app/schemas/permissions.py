from pydantic import BaseModel
from typing import Optional
from uuid import UUID
from datetime import datetime


class PermissionRead(BaseModel):
    id: UUID
    code: str
    description: Optional[str] = None
    created_at: datetime

    class Config:
        from_attributes = True


class PermissionCreate(BaseModel):
    code: str
    description: Optional[str] = None


class PermissionUpdate(BaseModel):
    code: Optional[str] = None
    description: Optional[str] = None
