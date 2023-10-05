from schemas.response import Response


class CustomException(Exception):
  def __init__(self, status: int, error: str = None, msg: str = None, body: dict = None):
    self.response = Response(status=status, error=error, msg=msg, body=body)
