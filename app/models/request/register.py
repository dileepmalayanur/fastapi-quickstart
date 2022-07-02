from pydantic import validator, Field

from app.models.request.base_request import BaseRequest
from app.utils.model_util import validate_field_email_address, validate_field_password


class RegisterBaseRequest(BaseRequest):
    email_address: str = Field(..., max_length=100)
    password: str = Field(..., min_length=8, max_length=12)

    @validator('email_address')
    def validate_email_address(cls, str):
        return validate_field_email_address(str)

    @validator('password')
    def validate_password(cls, str):
        return validate_field_password(str)
