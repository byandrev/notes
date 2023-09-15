import uvicorn
from fastapi import FastAPI

from core.settings import settings
from routers.base import router


def start_application():
  application: FastAPI = FastAPI(title=settings["PROJECT_NAME"],
                                 version=settings["PROJECT_VERSION"])
  application.include_router(router)
  return application


app = start_application()


if __name__ == "__main__":
  IS_RELOAD = settings["ENVIRONMENT"] == "development"
  uvicorn.run("main:app", host="0.0.0.0", port=settings.PORT, reload=IS_RELOAD)
