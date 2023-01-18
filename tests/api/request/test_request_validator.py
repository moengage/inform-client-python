import pytest

from informclient.api.request.request_validator import validate_request
from jsonschema.exceptions import ValidationError


def test_invalid_channel():
    payload = {
        "alert_id": "01234ABCDEF01234ABCDEF12",
        "transaction_id": "12346q13",
        "payloads":
            {
                "WHATSAPP":
                    {
                        "recipient": "+9112345678901",
                        "personalized_attributes": {
                            "attr": "value"
                        }
                    }
            }
    }
    with pytest.raises(ValidationError):
        validate_request(payload)


def test_missing_attr():
    payload = {
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
    with pytest.raises(ValidationError):
        validate_request(payload)


def test_invalid_request():
    payload = {
        "alert_id": "01234ABC",
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
    with pytest.raises(ValidationError):
        validate_request(payload)


def test_valid_request():
    payload = {
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
    validate_request(payload)
