
from sqlalchemy.orm import Session
from sqlalchemy.sql.functions import now

from app.constants.response_codes import FASTAPI_SUCCESS, FASTAPI_NEED_ACTIVATION, FASTAPI_USER_ALREADY_EXISTS
from app.database.entities.login import Login
from app.database.entities.profile import Profile
from app.enums.login_status import LoginStatus
from app.loader.properties import get_response_detail
from app.models.request.register import RegisterBaseRequest
from app.models.response.register import RegisterResponse
from app.services.service import FiService
from app.utils import secrets_util, email_util


class RegisterService(FiService):

    def validate(self, request: RegisterBaseRequest, db_session: Session) -> RegisterResponse:

        login_detail = db_session.query(Login).filter(Login.email_address == request.email_address).first()
        if login_detail is None:
            response = get_response_detail(FASTAPI_SUCCESS)
        elif login_detail.status == LoginStatus.PENDING_ACTIVATION.value:
            response = get_response_detail(FASTAPI_NEED_ACTIVATION)
            email_util.send_email(to_email_address=login_detail.email_address, subject='aa', body='bb')
        else:
            response = get_response_detail(FASTAPI_USER_ALREADY_EXISTS)

        return RegisterResponse(code=response[0], message=response[1])

    def process(self, request: RegisterBaseRequest, db_session: Session) -> RegisterResponse:

        new_login = Login()
        new_login.email_address = request.email_address
        new_login.password_hash = secrets_util.build_password_hash(request.password)
        new_login.status = LoginStatus.ACTIVE.value
        new_login.created_at = now()
        new_login.created_by = request.email_address

        new_profile = Profile()
        new_profile.login_parent = new_login
        new_profile.created_at = now()
        new_profile.created_by = request.email_address

        db_session.add(new_profile)
        db_session.flush()
        response = get_response_detail(FASTAPI_SUCCESS)

        return RegisterResponse(code=response[0], message=response[1])
