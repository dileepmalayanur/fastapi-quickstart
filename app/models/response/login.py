from typing import Optional

from app.models.response.base_response import Response


class LoginResponse(Response):
    auth_token: Optional[str] = None
