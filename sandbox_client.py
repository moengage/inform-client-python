from os import environ

from constants import APIDescription, InformRoutes
from exceptions import InformApiException
from session import InformAPISession

__version__ = '1.0.0'


class SandBoxClient(object):

    def __init__(self, base_url=None, auth_token=None, username=None, password=None, timeout=5, **kwargs):
        """
        Instantiate a new API client.
        Args:
          host (str): Hostname of Courier instance.
          auth_token (str): Auth Token used for Token Auth
          username (str): Username used for Basic Auth
          password (str): Password used for Basic Auth
          timeout (float|tuple): Timeout in seconds. (Connect, Read) Defaults
          to 5 seconds for both.
        """
        if base_url:
            self.base_url = base_url

        else:
            default_url = 'https://sandbox-inform-api-' + APIDescription.SUB_DOMAIN + '.moengage.com/' + APIDescription.VERSION + '/'
            self.base_url = environ.get('INFORM_BASE_URL', default_url)

        # Initialize the session.
        self.session = InformAPISession(timeout)
        self.session.init_library_version(__version__)

        # Token Auth takes precedence
        if auth_token:
            self.session.init_token_auth(auth_token)
        elif 'INFORM_AUTH_TOKEN' in environ:
            self.session.init_token_auth(environ['INFORM_AUTH_TOKEN'])

        # If no token auth, then Basic Auth
        elif username and password:
            self.session.init_basic_auth(username, password)
        elif 'INFORM_AUTH_USERNAME' in environ \
                and 'INFORM_AUTH_PASSWORD' in environ:
            username = environ.get('INFORM_AUTH_USERNAME', None)
            password = environ.get('INFORM_AUTH_PASSWORD', None)
            self.session.init_basic_auth(username, password)
