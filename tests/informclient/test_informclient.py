import pytest

from informclient import InformClient


def test_blank_base_url():
    with pytest.raises(ValueError):
        InformClient(base_url='', app_id='01234ABCDEFGHIJKLMNOPXYZ', api_secret='01234ABCDEFGHIJKLMNOPXYZ')


def test_blank_app_id():
    with pytest.raises(ValueError):
        InformClient(base_url='https://sandbox-inform-api-XX.moengage.com', app_id='', api_secret='123')


def test_blank_api_secret():
    with pytest.raises(ValueError):
        InformClient(base_url='https://sandbox-inform-api-XX.moengage.com', app_id='01234ABCDEF', api_secret='')


def test_valid_args():
    InformClient(base_url='https://sandbox-inform-api-XX.moengage.com', app_id='01234ABCDEF', api_secret='01234ABCDEF')