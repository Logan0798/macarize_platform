from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
import uuid

from app.models.base import Base


class UserRole(Base):
    __tablename__ = "user_roles"
    __table_args__ = {"schema": "crm_core"}

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    user_id = Column(
        UUID(as_uuid=True),
        ForeignKey("crm_core.users.id", ondelete="CASCADE"),
        nullable=False
    )

    role_id = Column(
        UUID(as_uuid=True),
        ForeignKey("crm_core.roles.id", ondelete="CASCADE"),
        nullable=False
    )
