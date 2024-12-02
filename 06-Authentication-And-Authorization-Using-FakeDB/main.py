from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from typing import Optional
from passlib.context import CryptContext
import jwt
from datetime import datetime, timedelta

# FastAPI application
app = FastAPI()

# OAuth2PasswordBearer is used to get the token from request header (Authorization: Bearer <token>)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Password context to hash passwords
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Secret key to encode/decode JWT tokens
SECRET_KEY = "mysecretkey"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Fake database (for demonstration purposes)
fake_users_db = {
    "user1": {
        "username": "user1",
        "hashed_password": pwd_context.hash("password123"),
        "email": "user1@example.com",
    }
}

# Step 1: Define the User model
class User(BaseModel):
    username: str
    email: Optional[str] = None

# Step 2: Define the Token model (JWT token format)
class Token(BaseModel):
    access_token: str
    token_type: str

# Step 3: Define the user creation logic (authentication)
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

# Step 4: Function to get a user from the fake database
def get_user_from_db(username: str):
    if username in fake_users_db:
        user_dict = fake_users_db[username]
        return User(username=username, email=user_dict["email"])

# Step 5: Function to create a JWT token
def create_access_token(data: dict, expires_delta: timedelta = timedelta(minutes=15)):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# Step 6: Route to login and get the token (Authentication)
@app.post("/token", response_model=Token)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = get_user_from_db(form_data.username)
    
    if not user or not verify_password(form_data.password, fake_users_db[form_data.username]["hashed_password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # Create a JWT token for the user
    access_token = create_access_token(data={"sub": form_data.username})
    return {"access_token": access_token, "token_type": "bearer"}

# Step 7: Protected route (Authorization)
@app.get("/users/me", response_model=User)
def read_users_me(current_user: User = Depends(oauth2_scheme)):
    return current_user
