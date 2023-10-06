from passlib.context import CryptContext

crypt_context = CryptContext(schemes=["bcrypt"])


class Hasher:
  @staticmethod
  def verify_password(plain_password: str, hashed_password: str) -> bool:
    return crypt_context.verify(plain_password, hashed_password)

  @staticmethod
  def generate_password(password: str) -> str:
    return crypt_context.hash(password)
