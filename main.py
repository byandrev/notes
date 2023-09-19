import uvicorn
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from fastapi.staticfiles import StaticFiles
from starlette.responses import RedirectResponse

from core.settings import settings
from db.client import engine
from routers.base import router
from app import models
from app.schemas.user import User
from app.database import SessionLocal, engine

models.Base.metadata.create_all(bind = engine)

def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()
  
def start_application():
  application: FastAPI = FastAPI(title=settings["PROJECT_NAME"],
                                 version=settings["PROJECT_VERSION"])
  application.mount("/static", StaticFiles(directory="static"), name="static")
  application.include_router(router)
  return application


app = start_application()

@app.post("/user/")
async def create_user(db: Session = Depends(get_db)):
  user = User()
  db.add(user)
  db.commit()
  response = RedirectResponse('/', status_code = 303)
  return response

if __name__ == "__main__":
  IS_RELOAD = settings["ENVIRONMENT"] == "development"
  uvicorn.run("main:app", host="0.0.0.0", port=settings["PORT"], reload=IS_RELOAD)
