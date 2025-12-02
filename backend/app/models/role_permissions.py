from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
import uuid

from app.models.base import Base


class RolePermission(Base):
    __tablename__ = "role_permissions"
    __table_args__ = {"schema": "crm_core"}

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    role_id = Column(
        UUID(as_uuid=True),
        ForeignKey("crm_core.roles.id", ondelete="CASCADE"),
        nullable=False
    )

    permission_id = Column(
        UUID(as_uuid=True),
        ForeignKey("crm_core.permissions.id", ondelete="CASCADE"),
        nullable=False
    )
