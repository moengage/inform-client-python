# This is for client end exceptions and not Inform-end
class InformClientException(Exception):

    def __init__(self, message, err_code=None):
        self.message = message
        self.err_code = err_code

    def get_message(self):
        return self.message
