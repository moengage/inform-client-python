from requests import Session


class InformAPISession(Session):

    def __init__(self):
        """
        Creates a new InformAPISession instance.
        """
        super(InformAPISession, self).__init__()

    def auth(self, username, password):
        pass
