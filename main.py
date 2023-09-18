import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from core import models
from core.settings import settings
from db.client import engine
from routers.base import router

models.Base.metadata.create_all(bind = engine)

def start_application():
  application: FastAPI = FastAPI(title=settings["PROJECT_NAME"],
                                 version=settings["PROJECT_VERSION"])
  application.mount("/static", StaticFiles(directory="static"), name="static")
  application.include_router(router)
  return application


app = start_application()


if __name__ == "__main__":
  IS_RELOAD = settings["ENVIRONMENT"] == "development"
  uvicorn.run("main:app", host="0.0.0.0", port=settings["PORT"], reload=IS_RELOAD)
