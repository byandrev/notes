from pydantic import BaseModel
from typing import Optional
from note import Note
from datetime import datetime
from typing import List

class User(BaseModel):
  id = Optional[int]
  first_name = str
  last_name = str
  birthday = datetime
  email = str
  email_confirmed = bool
  password = str
  notes = List[Note]
  created_at = datetime
  description = str
  profile_picture = str
  
  class Config:
    orm_mode = True