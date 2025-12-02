# app/models/base.py

# IMPORTANT:
# All models must share a single SQLAlchemy Base object.
# db.Base is the one Alembic and the ORM both use.
from app.core.db import Base

__all__ = ["Base"]
