from pydantic import BaseModel


class Response(BaseModel):
    code: str
    message: str
