from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import insert
from app.db import SessionLocal
from app.models.account import Account
from app.models.account_schema import AccountCreate

router = APIRouter(prefix="/accounts", tags=["accounts"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def create_account(payload: AccountCreate, db: Session = Depends(get_db)):

    stmt = insert(Account).values(
        name=payload.name,
        legal_name=payload.legal_name,
        website=payload.website,
        client_status_id=payload.client_status_id,
        lead_source_id=payload.lead_source_id,
        industry_id=payload.industry_id,
        notes=payload.notes,
    ).returning(Account)

    result = db.execute(stmt)
    db.commit()
    return result.fetchone()
