import abc

from sqlalchemy.orm import Session

from app.models.request.base_request import BaseRequest
from app.models.response.base_response import Response


class FiService(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def validate(self, request: BaseRequest, db_session: Session) -> Response:
        pass

    @abc.abstractmethod
    def process(self, request: BaseRequest, db_session: Session) -> Response:
        pass