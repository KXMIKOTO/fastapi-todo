from databases import Database
from sqlalchemy import create_engine
from app.models.models.task import Base

DATABASE_URL = "sqlite:///./todo.db"  # Example SQLite database URL
database = Database(DATABASE_URL)

engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

Base.metadata.create_all(bind=engine)