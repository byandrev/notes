from sqlalchemy import Boolean, Column, DateTime, Integer, String
# from sqlalchemy import Table, Boolean, Column, DateTime, ForeignKey, Integer, String
# from sqlalchemy.orm import relationship

from db.client import Base

# class Note(Base):
#   __tablename__ = 'note'
#   id = Column(Integer, primary_key = True)
#   title = Column(String(255))
#   content = Column(String(255))
#   created_at = Column(DateTime())
#   updated_at = Column(DateTime())
#   private = Column(Boolean())
#   tags = relationship('tag', secondary = 'note_tag', back_populates = 'notes')
#   collaborators = relationship('user', secondary = 'user_note', back_populates = 'notes')


# class Tag(Base):
#   __tablename__ = 'tag'
#   id = Column(Integer, primary_key = True)
#   name = Column(String(20))
#   notes = relationship('note', secondary = 'note_tag', back_populates = 'tags')

# note_tag = Table('note_tag', Base.metadata,
#                  Column('note_id', ForeignKey('note.id'), primary_key = True),
#                  Column('tag_id', ForeignKey('tag.id'), primary_key = True))


class User(Base):
  __tablename__ = 'user'
  id = Column(Integer, primary_key = True)
  first_name = Column(String(255))
  last_name = Column(String(255))
  birthday = Column(DateTime())
  email = Column(String(255))
  email_confirmed = Column(Boolean())
  password = Column(String(255))
  created_at = Column(DateTime())
  description = Column(String(255))
  profile_picture = Column(String(255))
  # notes = relationship('note', secondary = 'user_note', back_populates = 'collaborators')

# user_note = Table('user_note', Base.metadata,
#                   Column('user_id', ForeignKey('user.id'), primary_key = True),
#                   Column('note_id', ForeignKey('note.id'), primary_key = True))
