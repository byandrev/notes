from datetime import datetime
from sqlalchemy.orm import Session
from fastapi import APIRouter, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from db.client import get_db
from core.models import User, Note

templates = Jinja2Templates(directory="templates")

router = APIRouter()


@router.get("/", response_class=HTMLResponse)
def home(request: Request):
  return templates.TemplateResponse("index.html", {"request": request})


user = User(first_name="Andersson",
              last_name="---",
              birthday=datetime.now(),
              email="agmail.com",
              email_confirmed=False,
              password="12345",
              created_at=datetime.now(),
              description="Hola #2!",
              profile_picture="")

@router.get("/create-user")
async def create_user(database: Session = Depends(get_db)):
  database.add(user)
  database.commit()
  return user


@router.get("/users")
async def get_users(database: Session = Depends(get_db)):
  users = database.query(User).all()
  return users


@router.get("/notes")
async def get_notes(database: Session = Depends(get_db)):
  notes = database.query(Note).all()
  return notes
