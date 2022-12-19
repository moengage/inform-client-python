from strenum import StrEnum


class InformRoutes(StrEnum):
    INFORM_SEND = "send"


class DOMAIN(StrEnum):
    LIVE = 'https://inform-api-00.moengage.com/'
    TEST = 'https://sandbox-inform-api-00.moengage.com/'


class VERSION(StrEnum):
    v1 = 'v1'


class ERRCODE(StrEnum):
    ERR_400 = 'BAD_REQUEST'
    ERR_401 = 'UNAUTHORIZED'
    ERR_409 = 'DUPLICATE_REQUEST_RECEIVED'
    ERR_422 = '422 Unprocessable Entity'
    ERR_500 = '500 Internal Server Error'
    ERR_429 = 'RATE_LIMIT_REACHED'
