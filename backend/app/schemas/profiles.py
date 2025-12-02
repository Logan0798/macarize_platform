from pydantic import BaseModel
from typing import Optional
from uuid import UUID
from datetime import datetime


class UserProfileRead(BaseModel):
    id: UUID
    user_id: UUID
    job_title: Optional[str] = None
    department_id: Optional[UUID] = None
    location_id: Optional[UUID] = None
    manager_id: Optional[UUID] = None
    mobile_phone: Optional[str] = None
    time_zone: Optional[str] = None
    employment_type: Optional[str] = None
    cost_center: Optional[str] = None
    avatar_url: Optional[str] = None
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True


class UserProfileCreate(BaseModel):
    job_title: Optional[str] = None
    department_id: Optional[UUID] = None
    location_id: Optional[UUID] = None
    manager_id: Optional[UUID] = None
    mobile_phone: Optional[str] = None
    time_zone: Optional[str] = "UTC"
    employment_type: Optional[str] = None
    cost_center: Optional[str] = None
    avatar_url: Optional[str] = None


class UserProfileUpdate(BaseModel):
    job_title: Optional[str] = None
    department_id: Optional[UUID] = None
    location_id: Optional[UUID] = None
    manager_id: Optional[UUID] = None
    mobile_phone: Optional[str] = None
    time_zone: Optional[str] = None
    employment_type: Optional[str] = None
    cost_center: Optional[str] = None
    avatar_url: Optional[str] = None
