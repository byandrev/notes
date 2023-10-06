from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from core.settings import settings

DATABASE = f"{settings['DB_USER']}:{settings['DB_PASSWORD']}"
DATABASE += f"@{settings['DB_URL']}/{settings['DB_NAME']}"
DATABASE_URL = "mysql+mysqlconnector://" + DATABASE

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit = False, autoflush = False, bind = engine)

Base = declarative_base()

def get_db():
  database = SessionLocal()
  try:
    yield database
  finally:
    database.close()
