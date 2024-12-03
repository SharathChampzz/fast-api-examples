from fastapi import APIRouter
from logger import users_logger

router = APIRouter()

@router.get("/")
def get_users():
    users_logger.info("Fetching all users")
    return {"users": ["Alice", "Bob", "Charlie"]}

@router.get("/{user_id}")
def get_user(user_id: int):
    users_logger.debug(f"Fetching user with ID: {user_id}")
    if user_id < 0:
        users_logger.warning(f"Invalid user ID: {user_id}")
        return {"error": "Invalid user ID"}
    return {"user_id": user_id, "name": "Sample User"}
