# File Upload Example: Profile Picture Upload

## Overview
This example demonstrates how to handle file uploads using FastAPI. Users can upload a profile picture, which is saved to a designated folder with a unique filename based on the current timestamp.

### Key Concepts
1. **File Validation**:
   - The uploaded file is validated to ensure it is an image.
   - Files with unsupported formats are rejected.

2. **Unique Filename**:
   - The uploaded file is renamed to a unique filename using the current timestamp (`YYYYMMDDHHMMSS` format).

3. **Storage**:
   - Files are stored in a folder named `Profile Pictures`.

---

## Features
- **POST /upload-profile-picture/**:
  - Accepts an image file as input.
  - Renames the file based on the current timestamp.
  - Saves the file to the `Profile Pictures` folder.

---

## Required Modules
Install the following required module for FastAPI:
```bash
pip install fastapi[all]
