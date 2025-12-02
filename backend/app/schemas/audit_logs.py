from pydantic import BaseModel
from typing import Optional, Any
from uuid import UUID
from datetime import datetime


class AuditLogRead(BaseModel):
    id: UUID
    user_id: Optional[UUID] = None
    event_type: str
    event_data: Optional[Any] = None
    ip_address: Optional[str] = None
    created_at: datetime

    class Config:
        from_attributes = True


class AuditLogCreate(BaseModel):
    user_id: Optional[UUID] = None
    event_type: str
    event_data: Optional[Any] = None
    ip_address: Optional[str] = None
