from pydantic import BaseModel

from app.models.common.device import Device


class BaseRequest(BaseModel):
    request_id: str
    requester_id: str
    device: Device

