from sqlalchemy import Table, Boolean, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, mapped_column

from db.client import Base

user_note = Table("user_note",
                  Base.metadata,
                  Column("user_id", ForeignKey("user.id"), primary_key=True),
                  Column("note_id", ForeignKey("note.id"), primary_key=True),
                )

class Note(Base):
  __tablename__ = 'note'

  id = mapped_column(Integer, primary_key = True)
  title = Column(String(255))
  content = Column(String(255))
  created_at = Column(DateTime())
  updated_at = Column(DateTime())
  private = Column(Boolean())

  owner_id = mapped_column(ForeignKey("user.id"))
  owner = relationship("User", back_populates="notes")


class User(Base):
  __tablename__ = 'user'

  id = mapped_column(Integer, primary_key = True)
  first_name = Column(String(255))
  last_name = Column(String(255))
  birthday = Column(DateTime())
  email = Column(String(255))
  email_confirmed = Column(Boolean())
  password = Column(String(255))
  created_at = Column(DateTime())
  description = Column(String(255))
  profile_picture = Column(String(255))

  notes = relationship("Note", back_populates="owner")
