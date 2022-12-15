from api_client import InformAPIClient
from constants import APIDescription, HTTPMethod, InformRoutes
from inform_sent_request import SentRequest, TestSentRequest
from session import InformAPISession


class Inform(InformAPIClient):

    def __init__(self, username, password, **kwargs):
        super(Inform, self).__init__(username, password, **kwargs)
        # TODO auth
        self.auth_client = InformAPISession().auth(username, password)
        # TODO config
        # kwargs['server_url'] = 'http://' + ConfigProvider().get_server_url() + '/' + APIDescription.version + '/'
        self.http_client = InformAPIClient(db_name, **kwargs)

    def test_inform(self, request_data):
        """
        :param request_data:
        :return:
        """
        TestSentRequest(**request_data)
        return self.make_api_call_with_retry(http_method=HTTPMethod.POST, route_name=InformRoutes.INFORM_SEND,
                                             request_body=request_data)

    def send_inform(self, request_data):
        """
        :param request_data:
        :return:
        """
        SentRequest(**request_data)
        return self.make_api_call_with_retry(http_method=HTTPMethod.POST, route_name=InformRoutes.INFORM_SEND,
                                             request_body=request_data)