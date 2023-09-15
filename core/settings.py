import os
from pathlib import Path
from dotenv import load_dotenv

env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)


settings = {
  "PROJECT_NAME": "Notes",
  "PROJECT_VERSION": "1.0.0",
  "ENVIRONMENT": os.getenv("ENVIRONMENT"),
  "PORT": int(os.getenv("PORT"))
}
