import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from core.settings import settings
from routers.base import router


def start_application():
    application: FastAPI = FastAPI(title=settings.PROJECT_NAME,
                                   version=settings.PROJECT_VERSION)

    application.include_router(router)
    
    return application


app = start_application()

if __name__ == "__main__":
    is_reload = True if settings.ENVIRONMENT == "development" else False
    uvicorn.run("main:app", host="0.0.0.0", port=settings.PORT, reload=is_reload)