import datetime
from jose import jwt
from core.settings import settings


def create_access_token(data: dict):
  data_to_encode = data.copy()
  expire_time = datetime.datetime.utcnow() + datetime.timedelta(
      minutes=settings["ACCESS_TOKEN_EXPIRE_MINUTES"]
  )
  data_to_encode.update({"exp": expire_time})

  return jwt.encode(data_to_encode, settings["SECRET_KEY"], algorithm=settings["ALGORITHM"])


def decode_token(token: str):
  return jwt.decode(token, settings["SECRET_KEY"], algorithms=[settings["ALGORITHM"]])
