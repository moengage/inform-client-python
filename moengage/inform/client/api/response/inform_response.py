class InformClientResponse(object):

    def __init__(self, response):
        self.code = response.get('err_code', 'Success')
        self.message = response.get('message')
        self.request_id = response.get('request_id', None)
        self.request_type = response.get('request_type', None)

    def get_success_response(self):
        return {
            "code": self.code,
            "request_id": self.request_id,
            "message": self.message,
            "request_type": self.request_type
        }

    def get_error_response(self, status):
        if status == 400:
            return {
                "err_code": self.code,
                "message": self.message,
                "request_type": self.request_type
            }
        if status == 401:
            return {
                "err_code": self.code,
                "message": self.message
            }
        if status == 409:
            return {
                "err_code": self.code,
                "message": self.message,
                "request_type": self.request_type
            }
        if status == 429:
            return {
                "request_id": self.request_id,
                "err_code": self.code,
                "message": self.message,
                "request_type": self.request_type
            }
