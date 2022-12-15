class InformApiException(Exception):
    def __init__(self, err_type=None, attribute=None, message=None):
        self.response = {
            "error": {}
        }
        if err_type:
            self.response["error"]["type"] = err_type
        if attribute:
            self.response["error"]["attribute"] = attribute
        if message:
            self.response["error"]["message"] = message
