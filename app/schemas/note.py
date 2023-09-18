from pydantic import BaseModel
from user import User
from datetime import datetime
from tag import Tag
from typing import List

class Note(BaseModel):
  id = int
  title = str
  content = str
  created_at = datetime
  updated_at = datetime
  tags = List[Tag]
  private = bool
  collaborators = List[User]
  
  class Config:
    orm_mode = True
