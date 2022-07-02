from pydantic import validate_email

from app.constants.response_codes import FASTAPI_WRONG_EMAIL_ADDRESS, FASTAPI_WRONG_PASSWORD
from app.loader.properties import get_response_detail


def validate_field_email_address(email_address):
    try:
        validate_email(email_address)
    except:
        response = get_response_detail(FASTAPI_WRONG_EMAIL_ADDRESS)
        raise ValueError(response[1])

    return email_address


def validate_field_password(password):
    if len(password) < 8 or len(password) > 12:
        response = get_response_detail(FASTAPI_WRONG_PASSWORD)
        raise ValueError(response[1])

    return password