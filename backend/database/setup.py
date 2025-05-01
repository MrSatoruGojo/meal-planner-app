# backend/database/setup.py

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# SQLite DB file
DATABASE_URL = "sqlite:///mealplanner.db"

# Base class for models
Base = declarative_base()

# Create engine and session
engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine)
