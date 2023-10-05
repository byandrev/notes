from typing import Optional
from datetime import datetime
from pydantic import BaseModel


class User(BaseModel):
  id: Optional[int]
  first_name: str
  last_name: str
  birthday: datetime
  email: str
  created_at: datetime
  description: str
  profile_picture: str

  class Config:
    orm_mode = True


class UserIn(BaseModel):
  first_name: str
  last_name: str
  birthday: datetime
  email: str
  description: str
  profile_picture: str
  password: str


class UserInDB(User):
  hashed_password: str
  email_confirmed: bool


class UserResponse(User):
  pass
  