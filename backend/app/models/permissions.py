from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
import uuid

from app.models.base import Base


class Permission(Base):
    __tablename__ = "permissions"
    __table_args__ = {"schema": "crm_core"}

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    code = Column(String, unique=True, nullable=False)
    description = Column(String)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
