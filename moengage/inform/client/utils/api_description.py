from strenum import StrEnum


class HTTPMethod(StrEnum):
    """
    Enum class for HTTP METHOD supported by the client
    """
    POST = "POST"


class InformClientRoute(StrEnum):
    INFORM_SEND = "send"
