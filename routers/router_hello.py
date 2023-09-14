from typing import Union
from fastapi import APIRouter, Depends, status

router = APIRouter(prefix="/hello")

@router.get("/")
def hello():
  return "Hello"

