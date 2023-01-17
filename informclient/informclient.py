import json
import urllib3

from base64 import b64encode

from informclient.utils.api_description import InformClientRoutes
from informclient.api.request.request_validator import validate_request


class InformClient(object):

    def __init__(self, base_url, app_id, api_secret):
        """
        Instantiate a new Inform client.
        Args:
          base_url (str):
          app_id (str):
          api_secret (str):
        """
        if base_url == '' or app_id == '' or api_secret == '':
            raise ValueError("Any of the 3 required arguments: 'base_url', 'app_id', and 'api_secret' cannot be empty")
        self.base_url = base_url
        credentials = b64encode('{}:{}'.format(app_id, api_secret).encode())
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Basic {}'.format(credentials.decode()),
            'MOE-APPKEY': app_id
        }

    def send_alert(self, request_body):
        """
        Send alert to provided recipients
        Args:
            request_body:
        Returns:
            response: response of the Inform API
        """

        validate_request(request_body)

        url = "%s/%s" % (self.base_url, InformClientRoutes.INFORM_SEND)

        http = urllib3.PoolManager()
        encoded_body = json.dumps(request_body).encode('utf-8')
        resp = http.request("POST", url, body=encoded_body, headers=self.headers, timeout=10, retries=3)
        response = json.loads(resp.data.decode("utf-8"))

        return response
