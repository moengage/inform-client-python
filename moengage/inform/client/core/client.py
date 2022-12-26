import json
import urllib3
from base64 import b64encode

from moengage.inform.client.api.exception_handler import InformClientBaseException
from moengage.inform.client.utils.api_description import HTTPMethod, InformClientRoute


class BaseClient(object):

    def __init__(self, base_url=None, auth_token=None, username=None, password=None, **kwargs):
        """
        Instantiate a new API client.
        Args:
          base_url (str): Hostname of Client instance.
          auth_token (str): Auth Token used for Token Auth
          username (str): Username used for Basic Auth
          password (str): Password used for Basic Auth
        """
        self.base_url = base_url
        self.headers = {'content-type': 'application/json'}

        if auth_token:
            self.headers.update({
                'authorization': 'Bearer {}'.format(auth_token)
            })
        elif username and password:
            credentials = b64encode('{}:{}'.format(username, password).encode())
            self.headers.update({
                'authorization': 'Basic {}'.format(credentials.decode())
            })
            self.headers.update({
                'MOE-APPKEY': username
            })

    def send(self, request_body, **kwargs):
        """
        Post an inform request to Inform test/live  environment
        Args:
            request_body:
        Returns:
            dict: response of the Inform API
        """
        url = "%s/%s" % (self.base_url, InformClientRoute.INFORM_SEND)

        http = urllib3.PoolManager()
        encoded_body = json.dumps(request_body).encode('utf-8')
        resp = http.request(HTTPMethod.POST, url, body=encoded_body, headers=self.headers, timeout=5, retries=3)

        if resp.status >= 400:
            return json.loads(InformClientBaseException(resp.data, resp.status).get_message().decode('utf-8'))

        return json.loads(resp.data.decode('utf-8'))
