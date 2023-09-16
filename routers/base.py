from fastapi import APIRouter

from routers.router_hello import router as router_hello
from routers.router_home import router as router_home

router = APIRouter()

router.include_router(router_home)
router.include_router(router_hello)
