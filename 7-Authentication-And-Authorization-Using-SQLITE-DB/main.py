from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
import jwt
from datetime import datetime, timedelta
from . import crud, models, schemas, database

# FastAPI app initialization
app = FastAPI()

# OAuth2PasswordBearer is used to get the token from request header
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Secret key and algorithm for JWT
SECRET_KEY = "mysecretkey"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Dependency to get the database session
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Function to create JWT token
def create_access_token(data: dict, expires_delta: timedelta = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# Route to login and get the token
@app.post("/token", response_model=schemas.Token)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = crud.get_user_by_username(db, username=form_data.username)
    
    if not user or not crud.pwd_context.verify(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token = create_access_token(data={"sub": form_data.username})
    return {"access_token": access_token, "token_type": "bearer"}

# Protected route that requires authentication
@app.get("/users/me", response_model=schemas.User)
def read_users_me(current_user: schemas.User = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    user = crud.get_user_by_username(db, username=current_user.username)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
