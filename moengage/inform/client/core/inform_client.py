import json
import urllib3

from base64 import b64encode
from jsonschema.exceptions import ValidationError
from urllib3.exceptions import LocationValueError, ConnectTimeoutError, TimeoutError, MaxRetryError

from moengage.inform.client.utils.api_description import InformClientRoutes
from moengage.inform.client.api.request.request_validator import validate_request
from moengage.inform.client.api.response.inform_response import InformClientResponse


class InformClient(object):

    def __init__(self, base_url, app_id, api_secret):
        """
        Instantiate a new Inform client.
        Args:
          base_url (str):
          app_id (str):
          api_secret (str):
        """
        self.base_url = base_url
        credentials = b64encode('{}:{}'.format(app_id, api_secret).encode())
        self.headers = {
            'content-type': 'application/json',
            'authorization': 'Basic {}'.format(credentials.decode()),
            'MOE-APPKEY': app_id
        }

    def send(self, request_body):
        """
        Post an inform request to Inform environments
        Args:
            request_body:
        Returns:
            InformSentResponse: response of the Inform API
        """
        try:
            validate_request(request_body)
        except ValidationError as err:
            return err

        url = "%s/%s" % (self.base_url, InformClientRoutes.INFORM_SEND)

        try:
            http = urllib3.PoolManager()
            encoded_body = json.dumps(request_body).encode('utf-8')
            resp = http.request("POST", url, body=encoded_body, headers=self.headers, timeout=10)
            response = json.loads(resp.data.decode("utf-8"))
        except LocationValueError:
            return "Please Provide correct base_url"
        except (ConnectTimeoutError, TimeoutError):
            try:
                http = urllib3.PoolManager()
                encoded_body = json.dumps(request_body).encode('utf-8')
                resp = http.request("POST", url, body=encoded_body, headers=self.headers, timeout=10, retries=3)
                response = json.loads(resp.data.decode("utf-8"))
            except (ConnectTimeoutError, TimeoutError, MaxRetryError):
                return 'Connection failed to the provided server even after multiple retries'

        if resp.status == 200:
            return InformClientResponse(response).get_success_response()

        return InformClientResponse(response).get_error_response(resp.status)
