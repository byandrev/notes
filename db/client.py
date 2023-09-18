from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "mysql+mysqlconnector://root:ap2909@localhost:3306/notes_app"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit = False, autoflush = False, bind = engine)

Base = declarative_base()

def get_db():
  database = SessionLocal()
  try:
    yield database
  finally:
    database.close()
