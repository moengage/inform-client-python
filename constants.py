from strenum import StrEnum


class HTTPMethod(StrEnum):
    POST = 'POST'


class InformRoutes(StrEnum):
    INFORM_SEND = "send"


class APIDescription(StrEnum):
    version = 'v1'
