from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette.requests import Request

from app.constants.response_codes import FASTAPI_SUCCESS
from app.database.session_util import getDbSession
from app.interceptors.auth_interceptor import AuthInterceptor
from app.models.request.base_request import BaseRequest
from app.models.response.base_response import Response
from app.models.response.get_user import GetUserResponse
from app.services.get_user_service import GetUserService

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"],
    responses={404: {"description": "Not found"}},
    dependencies=[Depends(AuthInterceptor())]
)


@router.post("/get-user", response_model=Response)
async def get_user(request: Request, _base_request: BaseRequest,
                    db_session: Session = Depends(getDbSession)) -> GetUserResponse:
    service = GetUserService()
    response = service.validate(_base_request, db_session)
    if response.code == FASTAPI_SUCCESS:
        response = service.process(_base_request, db_session)

    return response
