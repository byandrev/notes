from datetime import datetime
from sqlalchemy.orm import Session
from fastapi import APIRouter, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from db.client import get_db
from core.models import User

templates = Jinja2Templates(directory="templates")

router = APIRouter()


@router.get("/", response_class=HTMLResponse)
def home(request: Request):
  return templates.TemplateResponse("index.html", {"request": request})


@router.get("/create-user")
async def create_user(database: Session = Depends(get_db)):
  user = User(first_name="Andres2",
              last_name="Parra2",
              birthday=datetime.now(),
              email="byandrev2@gmail.com",
              email_confirmed=False,
              password="12345",
              created_at=datetime.now(),
              description="Hola #2!",
              profile_picture="")
  database.add(user)
  database.commit()
  return user
