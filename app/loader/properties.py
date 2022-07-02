import os
import random, yaml

from app.constants.response_codes import FASTAPI_UNKNOWN_ERROR

with open("./resources/response-code.yml", "r") as stream:
    try:
        response_code_list = yaml.safe_load(stream)
    except yaml.YAMLError as e:
        print("Error loading response code configuration:", e)

with open("./resources/application.yml", "r") as stream:
    try:
        application_properties = yaml.safe_load(stream)
    except yaml.YAMLError as e:
        print("Error loading response code configuration:", e)


def get_response_detail(response_code: str):
    try:
        response_messages = response_code_list[response_code]
    except (IndentationError, KeyError):
        response_messages = response_code_list[FASTAPI_UNKNOWN_ERROR]

    return response_code, random.choice(response_messages['message'])


def get_response_message(response_code: str):
    try:
        response_messages = response_code_list[response_code]
    except (IndentationError, KeyError):
        response_messages = response_code_list[FASTAPI_UNKNOWN_ERROR]

    return random.choice(response_messages['message'])


def get_application_properties():
    return application_properties


def get_application_properties_value(property_name: str):
    application_properties_value = application_properties[property_name]
    application_properties_value = str(application_properties_value) if application_properties_value is not None else ''
    if str(application_properties_value).startswith('${') and str(application_properties_value).endswith('}'):
        application_properties_value = str(application_properties_value).removeprefix('${').removesuffix('}')
        application_properties_value = os.environ.get(application_properties_value)
    return application_properties_value

