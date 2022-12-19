import json
from os import environ

from constants import VERSION, InformRoutes
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
            default_url = 'https://sandbox-inform-api-00.moengage.com/' + VERSION.v1
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

    # Perform an API request
    def send(self, request_data, **kwargs):
        """
        Post an inform request to Inform SandBox test environment
        Args:
            request_data:
        Raises:
            InformApiException: Any error returned by the Inform API
        Returns:
            dict: response of the Inform API
        """

        url = "%s/%s" % (self.base_url, InformRoutes.INFORM_SEND)
        resp = self.session.post(url, data=json.dumps(request_data))
        if resp.status_code >= 400:
            raise InformApiException(resp)

        return resp.json()
