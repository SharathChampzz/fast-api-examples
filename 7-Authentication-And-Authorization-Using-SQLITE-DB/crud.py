from sqlalchemy.orm import Session
from . import models, schemas
from passlib.context import CryptContext

# Initialize password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Function to get a user by username
def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

# Function to create a new user
def create_user(db: Session, username: str, email: str, password: str):
    hashed_password = pwd_context.hash(password)
    db_user = models.User(username=username, email=email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
