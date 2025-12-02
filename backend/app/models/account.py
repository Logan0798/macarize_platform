from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.sql import func
from app.models.base import Base 

class Account(Base):
    __tablename__ = "account"
    __table_args__ = {"schema": "crm_core"}

    account_id = Column(Integer, primary_key=True, index=True)
    external_ref = Column(String)
    name = Column(String, nullable=False)
    legal_name = Column(String)
    website = Column(String)

    client_status_id = Column(Integer, ForeignKey("crm_ref.client_status.client_status_id"))
    lead_source_id = Column(Integer, ForeignKey("crm_ref.lead_source.lead_source_id"))
    industry_id = Column(Integer, ForeignKey("crm_ref.industry.industry_id"))

    is_active = Column(Boolean, default=True)
    notes = Column(String)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
