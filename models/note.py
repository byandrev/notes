from pydantic import BaseModel

class Note(BaseModel):
    id: int
    name: str
    content: str
    createdAt: str
    updateAt: str
    tags: list[str]
    private: bool
    colaborators: list[int]
    