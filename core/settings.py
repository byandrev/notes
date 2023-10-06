import os
from pathlib import Path
from dotenv import load_dotenv

env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)


settings = {
  "PROJECT_NAME": "Notes",
  "PROJECT_VERSION": "1.0.0",
  "ENVIRONMENT": os.getenv("ENVIRONMENT"),
  "PORT": int(os.getenv("PORT")),
  "DB_NAME": os.getenv("DB_NAME"),
  "DB_URL": os.getenv("DB_URL"),
  "DB_USER": os.getenv("DB_USER"),
  "DB_PASSWORD": os.getenv("DB_PASSWORD"),
  "ACCESS_TOKEN_EXPIRE_MINUTES": 1440,
  "SECRET_KEY": os.getenv("SECRET_KEY"),
  "ALGORITHM": "HS256"
}
