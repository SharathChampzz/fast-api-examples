from pydantic import BaseModel
from typing import Optional

# Pydantic models for input and output validation

# User data model
class User(BaseModel):
    username: str
    email: Optional[str] = None

    class Config:
        orm_mode = True

# Token data model (JWT)
class Token(BaseModel):
    access_token: str
    token_type: str
