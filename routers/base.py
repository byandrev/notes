from fastapi import APIRouter

from routers.router_hello import router as router_hello

router = APIRouter()

router.include_router(router_hello)