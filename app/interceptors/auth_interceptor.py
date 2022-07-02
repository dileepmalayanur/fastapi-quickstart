from typing import Mapping

from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jwcrypto.jwt import JWTExpired

from app.constants.app_constants import APP_PROPERTY_ENABLE_AUTHENTICATION, APP_PROPERTY_ONLINE_ENCRYPTION_KEY, \
    COOKIE_NAME_FASTAPI_AUTH
from app.constants.app_messages import APP_MESSAGE_INVALID_AUTHORIZATION_CODE, \
    APP_MESSAGE_INVALID_TOKEN_OR_EXPIRED_TOKEN, APP_MESSAGE_INVALID_AUTHENTICATION_SCHEME
from app.loader.properties import get_application_properties_value
from app.utils.common_util import parse_boolean
from app.utils.secrets_util import decrypt_auth_code


def verify_jwt(jw_token: str, key: str) -> bool:
    is_token_valid: bool = False
    try:
        payload = decrypt_auth_code(jw_token, key)
    except JWTExpired:
        payload = None
    if payload:
        is_token_valid = True
    return is_token_valid


class AuthInterceptor(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(AuthInterceptor, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        enable_authentication = get_application_properties_value(APP_PROPERTY_ENABLE_AUTHENTICATION)
        if parse_boolean(enable_authentication):
            online_encryption_key = get_application_properties_value(APP_PROPERTY_ONLINE_ENCRYPTION_KEY)
            cookie_value: Mapping = request.cookies.get(COOKIE_NAME_FASTAPI_AUTH)
            # Get JWT from HTTPOnly cookie, if not available, then get from 'Authorization' header.
            if cookie_value is None:
                credentials: HTTPAuthorizationCredentials = await super(AuthInterceptor, self).__call__(request)
                if credentials:
                    if not credentials.scheme.lower() == "bearer":
                        raise HTTPException(status_code=403, detail=APP_MESSAGE_INVALID_AUTHENTICATION_SCHEME)
                    if not verify_jwt(credentials.credentials, online_encryption_key):
                        raise HTTPException(status_code=403, detail=APP_MESSAGE_INVALID_TOKEN_OR_EXPIRED_TOKEN)
                else:
                    raise HTTPException(status_code=403, detail=APP_MESSAGE_INVALID_AUTHORIZATION_CODE)
            else:
                if not verify_jwt(cookie_value, online_encryption_key):
                    raise HTTPException(status_code=403, detail=APP_MESSAGE_INVALID_TOKEN_OR_EXPIRED_TOKEN)
