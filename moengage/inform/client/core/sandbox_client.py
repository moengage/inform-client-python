import json

from provider import InformClientConfigProvider
from moengage.inform.client.core.client import BaseClient
from moengage.inform.client.request.inform_sent_request import SandBoxClientSentRequest

from mongoengine.errors import FieldDoesNotExist, ValidationError


class SandBoxClient(BaseClient):

    def __init__(self, base_url=None, auth_token=None, username=None, password=None, **kwargs):
        if not base_url:
            base_url = InformClientConfigProvider().get_test_base_url()
        super().__init__(base_url, auth_token, username, password, **kwargs)

    def send(self, request_body, **kwargs):
        try:
            SandBoxClientSentRequest(**request_body).validate()
        except ValidationError as err:
            return err.errors
        except FieldDoesNotExist as err1:
            return json.dumps(str(err1))
        return super().send(request_body, **kwargs)
