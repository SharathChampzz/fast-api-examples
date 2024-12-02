# fast-api-examples
This repo contains various examples for fast Api

### Action Items:

# Level 1: Basics
#### Basic CRUD Operations:
Implement basic Create, Read, Update, Delete (CRUD) operations for a simple resource like Item or User.

#### Path and Query Parameters:
Create endpoints that combine path and query parameters, e.g., ```/search/items?name=book&price=20```.

#### JSON Request Body:
Accept structured JSON data using Pydantic models, such as creating a product with fields like name, price, and category.

# Level 2: Intermediate
#### Validation with Pydantic:
Add custom validation logic in your Pydantic models, such as ensuring a string has a minimum length or a number is within a range.

#### Dependency Injection:
Use FastAPI’s dependency injection system to share reusable logic, such as database connections or authentication tokens.

#### Nested Models:
Work with nested data models. For example, an Order might have a list of Items.

#### Response Models:
Define response models to control the structure of your API responses.

#### Custom Error Handling:
Create custom exception classes and handlers to return user-friendly error messages.

# Level 3: Advanced
#### Authentication & Authorization:
Implement JWT-based authentication, allowing users to log in and access protected routes.

#### Background Tasks:
Add background processing using FastAPI’s BackgroundTasks, e.g., sending an email after user registration.

#### File Uploads:
Create an endpoint to handle file uploads, such as uploading a profile picture.

#### WebSocket Communication:
Build a WebSocket endpoint for real-time communication, such as a chat application.

#### Rate Limiting:
Implement rate limiting for your API to prevent abuse, e.g., limit requests to 10 per minute.

# Level 4: Full-Fledged Applications
#### Database Integration:
Connect to a relational database (e.g., PostgreSQL, SQLite) using SQLAlchemy or Tortoise ORM. Build a resource like BlogPost with persistent storage.

#### Pagination and Filtering:
Add pagination and filtering to a list endpoint, e.g., fetching 10 users per page or filtering by username.

# Other Items

```Testing```: Write unit tests and integration tests for your endpoints using pytest.

```OAuth2 Login```: Allow users to authenticate via third-party services like Google or GitHub.

```API Versioning```: Implement API versioning (e.g., /v1/resource and /v2/resource).

```Caching```: Use caching mechanisms to improve performance, such as Redis.

```Async Tasks```: Integrate Celery or FastAPI’s async capabilities for heavy background jobs.