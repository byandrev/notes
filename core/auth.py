from typing import Union
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError

from core.hashing import Hasher
from core.security import decode_token
from schemas.user import User


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def get_current_user(token: str = Depends(oauth2_scheme)) -> User:
  try:
    payload = decode_token(token)
    username: str = payload.get("sub")

    if username is None:
      return None
  except JWTError:
    return None

  # user: User = User(**repository.get_user(username))
  user: User = None

  if user is None:
    return None

  return user


def authenticate_user(username: str, password: str) -> Union[User, bool]:
  # user = repository.get_user(username)
  print(username)
  user: User = None

  if user is None:
    return False

  # user_db: UserInDB = UserInDB(**user)
  user_db = None

  if not Hasher.verify_password(password, user_db.hashed_password):
    return False

  return User(**user_db.dict())
