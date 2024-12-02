## 1. Set Up Your Environment
Install Python: Ensure you have Python 3.7 or newer installed.

Check: ```python --version```
Create a Virtual Environment (optional but recommended):

```
python -m venv fastapi-env
source fastapi-env/bin/activate  # On Linux/Mac
fastapi-env\Scripts\activate    # On Windows
```

Install FastAPI and Uvicorn:

```
pip install fastapi uvicorn
```

## 2. Write the "Hello World" Code
Create a New Python File: Save the following code in a file named main.py.

```
from fastapi import FastAPI

# Create a FastAPI app instance
app = FastAPI()

# Define a simple route
@app.get("/")
def read_root():
    return {"message": "Hello, World!"}
```

## 3. Run the Application
Use Uvicorn, an ASGI server, to run the application:

```
uvicorn main:app --reload
```

Open your browser and go to:

http://127.0.0.1:8000/ to see the "Hello, World!" response.
http://127.0.0.1:8000/docs to view the automatically generated API documentation (powered by Swagger UI).

## 4. Project Structure
Your project should now look like this:

```
fastapi-project/
├── main.py
└── fastapi-env/  # Only if you used a virtual environment
```


## 5. Next Steps
Add more routes by using ```@app.get```, ```@app.post```, etc.
Explore the interactive API docs at /docs.
