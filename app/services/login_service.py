from sqlalchemy.orm import Session

from app.constants.app_constants import APP_PROPERTY_ENABLE_AUTHENTICATION, APP_PROPERTY_ONLINE_ENCRYPTION_KEY
from app.constants.response_codes import FASTAPI_SUCCESS, FASTAPI_NEED_ACTIVATION, FASTAPI_INVALID_ACCOUNT_STATE, \
    FASTAPI_CREDENTIALS_MISMATCH
from app.database.entities.login import Login
from app.enums.login_status import LoginStatus
from app.loader.properties import get_response_detail, get_application_properties_value
from app.models.request.login import LoginBaseRequest
from app.models.response.login import LoginResponse
from app.services.service import FiService
from app.utils import secrets_util, email_util


class LoginService(FiService):

    def validate(self, request: LoginBaseRequest, db_session: Session) -> LoginResponse:

        login_detail = db_session.query(Login).filter(Login.email_address==request.email_address).first()
        if login_detail is not None and login_detail.email_address == request.email_address and secrets_util.verify_password_hash(login_detail.password_hash, request.password):
            if login_detail.status == LoginStatus.ACTIVE.value:
                response = get_response_detail(FASTAPI_SUCCESS)
            elif login_detail.status == LoginStatus.PENDING_ACTIVATION.value:
                response = get_response_detail(FASTAPI_NEED_ACTIVATION)
                email_util.send_email(to_email_address=login_detail.email_address, subject='aa', body='bb')
            else:
                response = get_response_detail(FASTAPI_INVALID_ACCOUNT_STATE)
        elif login_detail is not None:
            response = get_response_detail(FASTAPI_CREDENTIALS_MISMATCH)
        else:
            response = get_response_detail(FASTAPI_CREDENTIALS_MISMATCH)

        return LoginResponse(code=response[0], message=response[1])

    def process(self, login_base_request: LoginBaseRequest, db_session: Session) -> LoginResponse:
        response = get_response_detail(FASTAPI_SUCCESS)
        _auth_token = None
        _enable_authentication = get_application_properties_value(APP_PROPERTY_ENABLE_AUTHENTICATION)
        if _enable_authentication:
            _online_encryption_key = get_application_properties_value(APP_PROPERTY_ONLINE_ENCRYPTION_KEY)
            _auth_token = secrets_util.generate_auth_code(login_base_request.email_address, _online_encryption_key)

        return LoginResponse(code=response[0], message=response[1], auth_token=_auth_token)
