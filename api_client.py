from apiclient import APIClient
from apiclient import RateLimiter
from exceptions import InformApiException
from retry import retry
from urllib3.exceptions import ConnectTimeoutError


class InformAPIClient(APIClient):

    def __init__(self, db_name, **kwargs):
        self.BASE_URL = kwargs['server_url']
        self.db_name = db_name
        self.retry_count = kwargs.pop('retry_count', 3)
        self.retry_interval = kwargs.pop('retry_interval', 10)
        self.lock = RateLimiter(max_messages=10, every_seconds=60)
        self.http_client = APIClient(rate_limit_lock=self.lock)

    @staticmethod
    def get_default_api_error_response(err_type=None, attribute=None, message=None):
        return InformApiException(err_type=err_type, attribute=attribute, message=message).response

    def make_api_call(self, http_method, route_name='send', **kwargs):
        try:
            kwargs['db_name'] = self.db_name
            return self.http_client.call(http_method=http_method, route_name=route_name, **kwargs)
        except Exception as err:
            raise err

    def make_api_call_with_retry(self, http_method, route_name, **kwargs):
        @retry(exceptions=(TimeoutError, ConnectTimeoutError), delay=self.retry_interval, times=self.retry_count)
        def execute_make_api_call():
            return self.make_api_call(http_method=http_method, route_name=route_name, **kwargs)

        return execute_make_api_call()
