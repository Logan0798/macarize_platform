from fastapi import FastAPI
from app.routers.accounts import router as accounts_router
from app.db import SessionLocal
from sqlalchemy import text

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Macarize CRM API running"}

app.include_router(accounts_router)

@app.get("/db-test")
def db_test():
    db = SessionLocal()
    result = db.execute(text("SELECT current_database();")).fetchone()
    db.close()
    return {"connected_database": result[0]}

