from pydantic import BaseModel

class Device(BaseModel):
    id: str
    ip_address: str
