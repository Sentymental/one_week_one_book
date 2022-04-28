"""
Database config file

- engine: database engine
- SessionLocal: local sessionmaker
- Base(): declarative_base
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Database URL:
DATABASE_URL = "sqlite:///./test.db"

# Database engine:
engine = create_engine(
    DATABASE_URL, connect_args={"check same thread": False}
)

# Sessionmaker:
SessionLocal = sessionmaker(
    autocommit=False,
    bind=engine
)

# Declarative Base:
Base = declarative_base()
