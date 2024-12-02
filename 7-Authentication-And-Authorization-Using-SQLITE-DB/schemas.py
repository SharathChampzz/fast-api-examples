from pydantic import BaseModel
from typing import Optional

# Pydantic models for input and output validation

# User data model
class UserBase(BaseModel):
    username: str
    email: str

    class Config:
        orm_mode = True  # This tells Pydantic to treat ORM models as dictionaries

class UserCreate(UserBase):
    password: str  # Password is required for creating the user, but not included in the response

class User(UserBase):
    id: int

    class Config:
        orm_mode = True  # This ensures the response is created from an ORM model

# Token data model (JWT)
class Token(BaseModel):
    access_token: str
    token_type: str
