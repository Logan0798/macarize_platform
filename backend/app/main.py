# from fastapi import FastAPI
# from app.routers.accounts import router as accounts_router
# from app.routers import users
# from app.db import SessionLocal
# from sqlalchemy import text
# from fastapi import FastAPI

# app = FastAPI()

# app.include_router(users.router)

# @app.get("/")
# def root():
#     return {"message": "Macarize CRM API running"}

# app.include_router(accounts_router)

# @app.get("/db-test")
# def db_test():
#     db = SessionLocal()
#     result = db.execute(text("SELECT current_database();")).fetchone()
#     db.close()
#     return {"connected_database": result[0]}

from fastapi import FastAPI
from app.routers.users import router as users_router

app = FastAPI()

app.include_router(users_router)

