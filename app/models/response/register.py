from typing import Optional

from app.models.response.base_response import Response


class RegisterResponse(Response):
    email_address: Optional[str] = None
