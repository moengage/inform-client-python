from moengage.inform.client.utils.constants import ERRCODE


class InformClientBaseException(Exception):

    def __init__(self, message, err_code):
        super(InformClientBaseException, self).__init__()
        self.message = message
        self.err_code = err_code

    def get_message(self):
        return self.message


class InformRetryableException(InformClientBaseException):
    def __init__(self, retry_count, message="Retry Exception", code=ERRCODE.ERR_500):
        super(InformRetryableException, self).__init__(message, code)
        self.retry_count = retry_count


class InformNonRetryableException(InformClientBaseException):
    def __init__(self, message="Non-Retry Exception", code=ERRCODE.ERR_500):
        super(InformNonRetryableException, self).__init__(message, code)


class UnhandledException(InformRetryableException):
    def __init__(self, retry_count, message="Unhandled Exception", code=ERRCODE.ERR_500):
        super(UnhandledException, self).__init__(retry_count, message, code)


class UnauthorizedException(InformClientBaseException):
    def __init__(self, message="Authorization Failed", code=ERRCODE.ERR_401):
        super(UnauthorizedException, self).__init__(message, code)


class InformReadException(InformClientBaseException):
    def __init__(self, message="Alert Not Available", code=ERRCODE.ERR_400):
        super(InformReadException, self).__init__(message, code)


class InvalidRequestException(InformNonRetryableException):
    def __init__(self, message="Invalid Request Exception", code=ERRCODE.ERR_422):
        super(InvalidRequestException, self).__init__(message, code)


class BadRequestException(InformNonRetryableException):
    def __init__(self, message="Invalid Connector Settings", code=ERRCODE.ERR_400):
        super(BadRequestException, self).__init__(message, code)


class RateLimitException(InformNonRetryableException):
    def __init__(self, message="Rate-Limit Reached", code=ERRCODE.ERR_429):
        super(RateLimitException, self).__init__(message, code)


class DeDuplicationException(InformNonRetryableException):
    def __init__(self, request_id, message="Duplicate Request", code=ERRCODE.ERR_409):
        super(DeDuplicationException, self).__init__(message, code)
        self.request_id = request_id


class InvalidFieldValueException(InformClientBaseException):
    def __init__(self, message="Invalid Field Value Exception", code=ERRCODE.ERR_400):
        super(InvalidFieldValueException, self).__init__(message, code)


class InvalidFieldException(InformClientBaseException):
    def __init__(self, message="Invalid Field Exception", code=ERRCODE.ERR_400):
        super(InvalidFieldException, self).__init__(message, code)
