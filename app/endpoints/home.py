from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette.requests import Request
from starlette.responses import RedirectResponse, Response

from app.cache.rate_limiter import limiter
from app.constants.app_constants import COOKIE_NAME_FASTAPI_AUTH, COOKIE_LIFETIME_IN_SECONDS
from app.database.session_util import getDbSession
from app.loader.properties import get_response_message, get_application_properties
from app.models.request.login import LoginBaseRequest
from app.models.request.register import RegisterBaseRequest
from app.models.response.login import LoginResponse
from app.models.response.register import RegisterResponse
from app.services.login_service import LoginService
from app.services.register_service import RegisterService
from app.constants.response_codes import FASTAPI_SUCCESS, FASTAPI_RATE_LIMIT_EXCEEDED
from app.utils.common_util import parse_boolean

router = APIRouter(
    tags=["Home"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def index():
    return RedirectResponse(url="/docs/")


@router.get("/health")
async def health():
    return {"status": "success"}


@router.post("/register", response_model=RegisterResponse)
@limiter.limit("5/minute", error_message=get_response_message(FASTAPI_RATE_LIMIT_EXCEEDED))
async def register(request: Request, register_base_request: RegisterBaseRequest,
                   db_session: Session = Depends(getDbSession)) -> RegisterResponse:
    service = RegisterService()
    response = service.validate(register_base_request, db_session)
    if response.code == FASTAPI_SUCCESS:
        response = service.process(register_base_request, db_session)

    return response


@router.post("/login", response_model=LoginResponse)
async def login(request: Request, response: Response, login_base_request: LoginBaseRequest,
                db_session: Session = Depends(getDbSession)) -> LoginResponse:
    service = LoginService()
    login_response = service.validate(login_base_request, db_session)
    if login_response.code == FASTAPI_SUCCESS:
        login_response = service.process(login_base_request, db_session)

    if login_response.code == FASTAPI_SUCCESS:
        response.set_cookie(
            key=COOKIE_NAME_FASTAPI_AUTH,
            value=login_response.auth_token,
            max_age=COOKIE_LIFETIME_IN_SECONDS,
            path='/',
            domain=get_application_properties()['cookie']['domain'],
            secure=parse_boolean(get_application_properties()['cookie']['secured']),
            httponly=True,
            samesite='lax')

    return login_response


