from strenum import StrEnum


class DOMAIN(StrEnum):
    LIVE = 'https://inform-api-00.moengage.com/'
    TEST = 'https://sandbox-inform-api-00.moengage.com/'


class VERSION(StrEnum):
    v1 = 'v1'
