class InformClientBaseException(Exception):

    def __init__(self, message, err_code):
        super(InformClientBaseException, self).__init__()
        self.message = message
        self.err_code = err_code

    def get_message(self):
        return self.message
