from moengage.inform.client.core.client import Client
from moengage.inform.client.utils.constants import DOMAIN, VERSION


class InformClient(Client):

    def __init__(self, base_url=None, auth_token=None, username=None, password=None, **kwargs):
        if not base_url:
            base_url = DOMAIN.LIVE + VERSION.v1
        super().__init__(base_url, auth_token, username, password, **kwargs)
