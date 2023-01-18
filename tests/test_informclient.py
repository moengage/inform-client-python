import unittest

import pytest

from unittest.mock import patch
from informclient import InformClient


class TestInformClient(unittest.TestCase):

    def test_blank_base_url(self):
        with pytest.raises(ValueError):
            InformClient(base_url='', app_id='01234ABCDEFGHIJKLMNOPXYZ', api_secret='01234ABCDEFGHIJKLMNOPXYZ')

    def test_blank_app_id(self):
        with pytest.raises(ValueError):
            InformClient(base_url='https://sandbox-inform-api-XX.moengage.com', app_id='', api_secret='123')

    def test_blank_api_secret(self):
        with pytest.raises(ValueError):
            InformClient(base_url='https://sandbox-inform-api-XX.moengage.com', app_id='01234ABCDEF', api_secret='')

    def test_valid_args(self):
        InformClient(base_url='https://sandbox-inform-api-XX.moengage.com',
                     app_id='01234ABCDEF',
                     api_secret='01234ABCDEF')

    def test_send_alert(self):
        mock_response = {"message": "alert submitted"}
        with patch('informclient.InformClient.send_alert') as mock_send_alert:
            mock_send_alert.return_value.status_code = 200
            mock_send_alert.return_value.json.return_value = mock_response
            c = InformClient(base_url='https://sandbox-inform-api-00.moengage.com',
                             app_id='01234ABCDEF',
                             api_secret='01234ABCDEF')
            body = {
                "alert_id": "01234ABCDEF01234ABCDEF12",
                "transaction_id": "12346q13",
                "payloads":
                    {
                        "SMS":
                            {
                                "recipient": "+9112345678901",
                                "personalized_attributes": {
                                    "attr": "value"
                                }
                            }
                    }
            }

            response = c.send_alert(body)
            response = mock_response

        assert response == mock_response
