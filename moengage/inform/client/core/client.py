import json
import urllib3
from base64 import b64encode
from os import environ

from moengage.inform.client.api.exception_handler import InformClientBaseException
from moengage.inform.client.utils.constants import InformRoutes


class Client(object):

    def __init__(self, base_url=None, auth_token=None, username=None, password=None, **kwargs):
        """
        Instantiate a new API client.
        Args:
          host (str): Hostname of Courier instance.
          auth_token (str): Auth Token used for Token Auth
          username (str): Username used for Basic Auth
          password (str): Password used for Basic Auth
          timeout (float|tuple): Timeout in seconds. (Connect, Read) Defaults to 5 seconds for both.
        """
        # Initialize the base url and headers
        self.base_url = environ.get('INFORM_BASE_URL', base_url)
        self.headers = {'content-type': 'application/json'}

        # Token Auth takes precedence
        if auth_token or 'INFORM_AUTH_TOKEN' in environ:
            self.headers.update({
                'authorization': 'Bearer {}'.format(auth_token)
            })

        # If no token auth, then Basic Auth
        elif (username and password) or ('INFORM_AUTH_USERNAME' in environ and 'INFORM_AUTH_PASSWORD' in environ):
            credentials = b64encode('{}:{}'.format(username, password).encode())
            self.headers.update({
                'authorization': 'Basic {}'.format(credentials.decode())
            })
            self.headers.update({
                'MOE-APPKEY': username
            })

    # Perform an API request
    def send(self, request_body, **kwargs):
        """
        Post an inform request to Inform live  environment
        Args:
            request_body:
        Raises:
            InformClientBaseException: Any error returned by the Inform API
        Returns:
            dict: response of the Inform API
        """

        url = "%s/%s" % (self.base_url, InformRoutes.INFORM_SEND)

        http = urllib3.PoolManager()
        encoded_body = json.dumps(request_body).encode('utf-8')
        resp = http.request('POST', url, body=encoded_body, headers=self.headers)

        if resp.status >= 400:
            return json.loads(InformClientBaseException(resp.data, resp.status).get_message().decode('utf-8'))

        return json.loads(resp.data.decode('utf-8'))
