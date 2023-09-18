from pydantic import BaseModel
from models.note import Note

class User(BaseModel):
  id: int
  firstName : str
  lastName: str
  birthday: str
  email : str
  emailConfirmed: bool
  password: str
  dailyNote: Note #Para la clase Note
  createdAt: str
  updatedAt: str
  description: str
  profilePicture: str
  