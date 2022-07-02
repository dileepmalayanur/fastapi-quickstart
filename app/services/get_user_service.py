from sqlalchemy.orm import Session

from app.constants.app_constants import APP_PROPERTY_ENABLE_AUTHENTICATION, APP_PROPERTY_ONLINE_ENCRYPTION_KEY
from app.constants.response_codes import FASTAPI_SUCCESS, FASTAPI_NEED_ACTIVATION, FASTAPI_INVALID_ACCOUNT_STATE, \
    FASTAPI_CREDENTIALS_MISMATCH
from app.database.entities.login import Login
from app.enums.login_status import LoginStatus
from app.loader.properties import get_response_detail, get_application_properties_value
from app.models.request.login import LoginBaseRequest
from app.models.response.get_user import GetUserResponse
from app.models.response.login import LoginResponse
from app.services.service import FiService
from app.utils import secrets_util, email_util


class GetUserService(FiService):

    def validate(self, request: LoginBaseRequest, db_session: Session) -> GetUserResponse:

        response = get_response_detail(FASTAPI_SUCCESS)
        return GetUserResponse(code=response[0], message=response[1])

    def process(self, login_base_request: LoginBaseRequest, db_session: Session) -> GetUserResponse:
        response = get_response_detail(FASTAPI_SUCCESS)
        '''
            Query database here and set the response.
        '''

        return GetUserResponse(code=response[0], message=response[1])
