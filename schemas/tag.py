from pydantic import BaseModel
from typing import Optional

class Tag(BaseModel):
  id: Optional[int]
  name: str

  class Config:
    orm_mode = True
