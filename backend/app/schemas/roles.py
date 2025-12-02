from pydantic import BaseModel
from typing import Optional
from uuid import UUID
from datetime import datetime


class RoleRead(BaseModel):
    id: UUID
    name: str
    description: Optional[str] = None
    is_system_role: bool
    created_at: datetime

    class Config:
        from_attributes = True


class RoleCreate(BaseModel):
    name: str
    description: Optional[str] = None


class RoleUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    is_system_role: Optional[bool] = None
