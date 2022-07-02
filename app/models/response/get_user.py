from typing import Optional

from app.models.response.base_response import Response


class GetUserResponse(Response):
    first_name: Optional[str] = None
    middle_name: Optional[str] = None
    last_name: Optional[str] = None
    gender_code: Optional[str] = None
    country_code: Optional[str] = None
