from typing import List
from datetime import datetime
from pydantic import BaseModel

from schemas.user import User
from schemas.tag import Tag

class Note(BaseModel):
  title: str
  content: str
  created_at: datetime
  updated_at: datetime
  tags: List[Tag]
  private: bool
  collaborators: List[User]

  class Config:
    orm_mode = True
