from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the database URL
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

# Create the database engine
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

# Create the session local (used for dependency injection)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Define the base class for all models
Base = declarative_base()
