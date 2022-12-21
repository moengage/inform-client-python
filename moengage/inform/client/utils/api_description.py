from strenum import StrEnum


class HTTPMethod(StrEnum):
    """
    Enum class for HTTP METHOD supported by the client
    """
    POST = "POST"


class InformServiceRouteName(StrEnum):
    INFORM_SENT = "send"
