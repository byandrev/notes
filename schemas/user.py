from typing import Optional
from datetime import datetime
from pydantic import BaseModel


class User(BaseModel):
  id: Optional[int]
  first_name: str
  last_name: str
  birthday: datetime
  email: str
  email_confirmed: bool
  password: str
  created_at: datetime
  description: str
  profile_picture: str

  class Config:
    orm_mode = True
