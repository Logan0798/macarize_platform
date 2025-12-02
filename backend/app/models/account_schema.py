from pydantic import BaseModel

class AccountCreate(BaseModel):
    name: str
    legal_name: str | None = None
    website: str | None = None
    client_status_id: int | None = None
    lead_source_id: int | None = None
    industry_id: int | None = None
    notes: str | None = None
