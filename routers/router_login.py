from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")

router = APIRouter(prefix="/login")

@router.get("/", response_class=HTMLResponse)
def home(request: Request):
  return templates.TemplateResponse("login.html", {"request": request})
