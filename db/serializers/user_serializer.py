def user_entity(user) -> dict:
  return {
    "id": str(user["_id"]),
    "username": user["username"],
    "email": user["email"],
    "hashed_password": user["hashed_password"]
  }
