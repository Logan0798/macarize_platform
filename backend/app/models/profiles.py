from sqlalchemy import Column, String, DateTime, Text, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
import uuid

from app.models.base import Base


class UserProfile(Base):
    __tablename__ = "user_profiles"
    __table_args__ = {"schema": "crm_core"}

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    user_id = Column(UUID(as_uuid=True), ForeignKey("crm_core.users.id", ondelete="CASCADE"), unique=True)

    job_title = Column(String)
    department_id = Column(UUID(as_uuid=True), ForeignKey("crm_ref.departments.id"))
    location_id = Column(UUID(as_uuid=True), ForeignKey("crm_ref.locations.id"))
    manager_id = Column(UUID(as_uuid=True), ForeignKey("crm_core.users.id"))

    mobile_phone = Column(String)
    time_zone = Column(String, default="UTC")
    employment_type = Column(String)
    cost_center = Column(String)
    avatar_url = Column(Text)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
