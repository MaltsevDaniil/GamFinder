from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .schemas import Base

SQLALCHEMY_DATABASE_URL = "sqlite:///users/test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)

Base.metadata.create_all(bind=engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)