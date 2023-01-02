import urllib3

from base64 import b64encode
from jsonschema.exceptions import ValidationError

from moengage.inform.client.api.exception_handler import InformClientException
from moengage.inform.client.utils.api_description import InformClientRoutes
from moengage.inform.client.api.request.request_validator import validate_request


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
        import json
        try:
            validate_request(request_body)
        except ValidationError as err:
            # 422 Unprocessable Entity
            return err
        url = "%s/%s" % (self.base_url, InformClientRoutes.INFORM_SEND)

        http = urllib3.PoolManager()
        encoded_body = json.dumps(request_body).encode('utf-8')
        try:
            resp = http.request("POST", url, body=encoded_body, headers=self.headers, timeout=10)
        except Exception as e:
            print(e)

        if resp.status >= 400:
            return resp.data, resp.status

        import json

        data = {}
        data['key'] = 'value'
        #json_data = json.dumps(data)

        return json.loads(resp.data.decode('utf-8'))
