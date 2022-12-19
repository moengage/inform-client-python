import json
import re

from moengage.inform.client.utils.constants import ERRCODE
from moengage.inform.client.utils.exceptions import InformReadException, BadRequestException, UnauthorizedException, \
    RateLimitException, DeDuplicationException, InvalidFieldValueException, InvalidFieldException


class InformExceptionHandler(object):
    def handle(self, ex, resp):
        if isinstance(ex, InformReadException):
            resp.status = ERRCODE.ERR_400
            resp.body = json.dumps({
                "message": ex.message, "err_code": ex.err_code
            })
        elif isinstance(ex, BadRequestException):
            resp.status = ERRCODE.ERR_400
            resp.body = json.dumps({
                "message": ex.message, "err_code": ex.err_code
            })
        elif isinstance(ex, UnauthorizedException):
            resp.status = ERRCODE.ERR_401
            resp.body = json.dumps({"message": ex.message, "err_code": ex.err_code})
        elif isinstance(ex, RateLimitException):
            resp.status = ERRCODE.ERR_429
            resp.body = json.dumps({
                "message": ex.message, "err_code": ex.err_code
            })
        elif isinstance(ex, DeDuplicationException):
            resp.status = ERRCODE.ERR_409
            resp.body = json.dumps({
                "message": ex.message, "err_code": ex.err_code,
                "request_id": ex.request_id
            })
        elif isinstance(ex, InvalidFieldValueException):
            resp.status = ERRCODE.ERR_400
            resp.body = json.dumps({
                "message": ex.message.replace(' : None', ''),
                "err_code": "BAD_REQUEST"
            })
        elif isinstance(ex, InvalidFieldException):
            resp.status = ERRCODE.ERR_400
            match = re.search("\[\\'(.*)\\'\]", ex.message)
            message = 'Invalid field(s) in the request'
            if match:
                message += ' : [' + match.group(1) + ']'

            resp.body = json.dumps({
                "message": message,
                "err_code": "BAD_REQUEST"
            })
        else:
            resp.status = ERRCODE.ERR_500
            resp.body = json.dumps({
                "message": 'Exception occurred, Please contact MoEngage',
                "err_code": "INTERNAL_SERVER_ERROR"
            })
