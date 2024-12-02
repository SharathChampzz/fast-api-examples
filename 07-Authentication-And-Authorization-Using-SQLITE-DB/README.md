# FastAPI Authentication and Authorization with SQLite

This project demonstrates how to implement **authentication** and **authorization** in a FastAPI application using JWT tokens and SQLite as the database.

---

## **Basic Concepts to Understand the Code**

### **1. Authentication**
Authentication is the process of verifying a user's identity. In this example, users provide their username and password, and if valid, a JWT token is generated and returned.

- **OAuth2PasswordBearer**: FastAPI uses this to retrieve the token from the request header.
- **JWT (JSON Web Token)**: After successful authentication, a JWT token is generated and sent to the user. This token will be used to authorize future requests.

### **2. Authorization**
Authorization ensures that an authenticated user can access specific resources or endpoints. Only users with a valid JWT token can access protected routes.

- **JWT Token**: The token contains the user's identity and is used to authenticate requests to the protected routes.
  
### **3. Database Integration**
The project uses **SQLite** to store user data (including hashed passwords). The database is queried to validate user credentials and retrieve user information for protected routes.

### **4. Hashing Passwords**
Passwords are hashed using **bcrypt** via the `passlib` library before storing them in the database. This ensures that passwords are not stored as plain text.

---

## **Required Dependencies**

To install the required modules, run the following command:

```pip install fastapi[all] sqlalchemy pydantic passlib python-jose```

This will install all the necessary dependencies for running the app, including FastAPI, SQLAlchemy for database interaction, Pydantic for validation, and passlib for password hashing.

---

## **What the Code Does**
- /token: This route handles authentication. It checks the user's credentials and, if valid, returns a JWT token.

- /users/me: This is a protected route that requires a valid JWT token. The token is used to verify the user's identity and return user details.

- Database: User information, including hashed passwords, is stored in an SQLite database. This database is queried to verify user credentials and fetch user data.

This project illustrates how to implement secure authentication and authorization with JWT tokens and SQLite in a FastAPI application.


---

### **Explanation of Changes**
- **Database Integration**: Now, the authentication and authorization system uses an actual SQLite database (created with SQLAlchemy) for storing user data.
- **CRUD Operations**: The logic for interacting with the database (e.g., creating and retrieving users) is implemented in a separate file (`crud.py`) for better organization.
- **Dependency Injection**: We inject the database session using the `get_db` dependency to avoid manually handling the session in each route.

### **Key Points**
- **SQLite Database**: The application now uses an actual SQLite database (`test.db`) to store users and their hashed passwords.
- **Token-Based Authentication**: Users authenticate by sending their credentials to the `/token` route. On success, they receive a JWT token to use in subsequent requests.
- **Protected Route**: The `/users/me` route is protected, meaning only users with a valid JWT token can access it.
