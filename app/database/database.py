from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from app.core.config import DATABASE_URL

assert DATABASE_URL is not None, "DATABASE_URL must be configured"

engine = create_engine(
    DATABASE_URL,
    echo = True,
)

class Base(DeclarativeBase):
    pass    