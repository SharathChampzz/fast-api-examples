# main.py
from fastapi import FastAPI, File, UploadFile, HTTPException
from pathlib import Path
from datetime import datetime

app = FastAPI()

# Directory to store profile pictures
UPLOAD_DIR = Path("Profile Pictures")
UPLOAD_DIR.mkdir(exist_ok=True)  # Create the directory if it doesn't exist

@app.post("/upload-profile-picture/")
async def upload_profile_picture(file: UploadFile = File(...)):
    # Validate file type
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="Invalid file type. Only images are allowed.")

    # Generate unique filename with the current timestamp
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    file_extension = Path(file.filename).suffix
    unique_filename = f"{timestamp}{file_extension}"

    # Save the file
    file_path = UPLOAD_DIR / unique_filename
    with open(file_path, "wb") as f:
        f.write(await file.read())

    return {"filename": unique_filename, "message": "Profile picture uploaded successfully"}
