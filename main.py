from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi import Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from pydantic import BaseModel

# Define the database connection parameters
DATABASE_URL = "postgresql://user:password@localhost/dbname"

# Create the database engine
engine = create_engine(DATABASE_URL)

# Create a configured "Session" class
Session = sessionmaker(bind=engine)

# Create a base class for declarative class definitions
Base = declarative_base()

# Define a simple user model
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)

# Create the database tables
Base.metadata.create_all(engine)

# Define a Pydantic model for the user
class UserModel(BaseModel):
    id: int
    name: str
    email: str

# Create the FastAPI app
app = FastAPI()

# Define a dependency to get a database session
def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()

# Define a route to get all users
@app.get("/users/")
def read_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return JSONResponse(content=[user.name for user in users], media_type="application/json")
