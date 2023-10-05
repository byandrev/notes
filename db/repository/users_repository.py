from typing import Union

from db.serializers.user_serializer import user_entity
from schemas.user import UserInDB, UserIn, UserResponse
from core.hashing import Hasher

users = db.get_collection("users")


def add(user: UserIn) -> Union[UserResponse, None]:
  to_insert = {
    "username": user.username,
    "email": user.email,
    "hashed_password": Hasher.generate_password(user.password)
  }
  inserted = users.insert_one(to_insert)
  inserted_id = inserted.inserted_id
  user_inserted = users.find_one({"_id": inserted_id})
  return user_entity(user_inserted)


def get_user(username: str) -> Union[UserInDB, None]:
  try:
    user = users.find_one({"email": username})
    return user_entity(user)
  except:
      return None
