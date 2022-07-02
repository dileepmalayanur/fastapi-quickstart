from enum import Enum


class LoginStatus(Enum):
    ACTIVE = 'A'
    PENDING_ACTIVATION = 'P'
    SUSPENDED = 'S'
    DELETED = 'D'
