from pydantic import BaseModel
from models.note import Note

class Tag(BaseModel):
  id: int
  name: str
  notes: list[Note]
