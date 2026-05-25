from pydantic import BaseModel

class UserModel(BaseModel):
    id: int
    name: str
    email: str
```

**DOCUMENTATION:**

### FastAPI/PostgreSQL Boilerplate

This boilerplate provides a basic structure for building a FastAPI application with a PostgreSQL database.

#### Dependencies

* `fastapi`
* `sqlalchemy`
* `pydantic`
* `pg8000`

#### Database Configuration

The database connection parameters are defined in the `main.py` file. You will need to replace the placeholders with your actual database credentials.

#### Models

The `models.py` file defines the database models using SQLAlchemy. The `User` model is a simple example of a user entity.

#### Schemas

The `schemas.py` file defines the Pydantic models for the API. The `UserModel` schema is used to validate and serialize the user data.

#### API Endpoints

The `main.py` file defines a single API endpoint to get all users. The endpoint uses the `get_db` dependency to get a database session and queries the `User` model to retrieve all users.

### Running the Application

To run the application, navigate to the project directory and execute the following command:

[CMD]
```bash
uvicorn main:app --host 0.0.0.0 --port 8000
