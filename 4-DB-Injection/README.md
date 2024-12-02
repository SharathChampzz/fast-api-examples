# FastAPI SQLite Integration with Dependency Injection
This project demonstrates how to integrate FastAPI with SQLite for database operations using SQLAlchemy. It also introduces dependency injection, a fundamental concept in FastAPI, which simplifies how database sessions are managed.

## What is Database Injection?
Database injection in FastAPI refers to the use of dependency injection to manage database sessions. Instead of manually handling connections in every function, we define a reusable ```get_db``` function that:

Creates a database session.
Ensures the session is closed after each request, even if an error occurs.
This approach:

1. Keeps the code clean and reusable.

2. Prevents issues like database locks due to unclosed sessions.

3. Makes it easy to integrate other dependencies like authentication or caching.

## What is Happening in This Script?

### Database Setup:

SQLite is used as the database, with SQLAlchemy as the ORM (Object Relational Mapper).
A database table named ```items``` is created with the following fields:

```id``` (primary key)

```name``` (string, item name)

```price``` (float, item price)

```description``` (string, optional, default: "No description provided")

### Database Dependency (get_db):

This function creates and manages the database session for every request.
It is used in all endpoints that need database access by injecting it as a dependency.

```    
def get_db():
    db = SessionLocal()  # Creates a database session
    try:
        yield db  # Passes the session to the endpoint
    finally:
        db.close()  # Closes the session after use
```

### CRUD Operations:

```Create```: Adds a new item to the database.

```Read```: Retrieves all items or a specific item by ID.

```Update```: Modifies an existing item's details.

```Delete```: Removes an item from the database.

### How the Endpoints Work:

For each endpoint, the database session (db) is injected using Depends(get_db).
The session is then used to query, insert, update, or delete records from the database.

Example:


```
@app.get("/items/")
def get_items(db: Session = Depends(get_db)):
    items = db.query(Item).all()  # Queries all items
    return [{"id": item.id, "name": item.name, "price": item.price, "description": item.description} for item in items]
```

## How It Works
### Start the App:

Run the application using uvicorn:
```uvicorn main:app --reload```

This starts the FastAPI server and creates the SQLite database (test.db) if it doesn't already exist.


### Database Operations:

When you interact with an endpoint, FastAPI:
1. Calls get_db to provide a database session.
2. Executes the requested operation (e.g., create, read, update, or delete).
3. Automatically closes the session after the operation.

### Documentation:

FastAPI automatically generates interactive API documentation, available at /docs (Swagger UI).

## Why Use Dependency Injection?

```Simplicity```: Avoid boilerplate code for managing database sessions.

```Consistency```: Use a single session across multiple database operations in a request.

```Error Handling```: Ensures sessions are properly closed, preventing resource leaks.

```Scalability```: Easily extend the logic (e.g., logging or authentication) by adding new dependencies.