from fastapi import APIRouter

from routers.router_hello import router as router_hello
from routers.router_home import router as router_home
from routers.router_login import router as router_login
from routers.router_register import router as router_register
from routers.router_signin import router as router_signin
from routers.router_editor import router as router_editor

router = APIRouter()

router.include_router(router_home)
router.include_router(router_hello)
router.include_router(router_login)
router.include_router(router_signin)
router.include_router(router_register)
router.include_router(router_editor)
