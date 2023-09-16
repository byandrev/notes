from pydantic import BaseModel
from models import Note

class Tag(BaseModel):
    id: int
    name: str
    notes: list[Note]