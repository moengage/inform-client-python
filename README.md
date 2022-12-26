# `inform-client-python`

This Python Package helps you send notifications through [MoEngage Inform](https://www.moengage.com/blog/introducing-transactional-alerts-moengage-inform/), the smartest way to design &amp; deliver notifications. Deliver your transactional messages to any channel through one API. Currently Email and SMS channels are supported.

APIs supported:

- Inform Test API
- Inform Send API

## Official Inform API docs

For a full description of request and response payloads and properties, please see the [official Inform API docs](https://help.moengage.com/hc/en-us/articles/10672957787284-Overview-Inform).

## Usage

### Using Token Auth

#### Inform Test Client

```python
from moengage.inform.client.core.sandbox_client import SandBoxClient

client = SandBoxClient(auth_token="your-auth-token")

payload = {"alert_id": "test_alert_id","user_id": "test_user_id","transaction_id": "test_transaction_id","payloads": {"SMS": {"recipient":"samplemobileno","personalized_attributes": {"attr": "value"}}}}
response = client.send(payload)
print(response)
```

#### Inform Live Client

```python
from moengage.inform.client.core.inform_client import InformClient

client = InformClient(auth_token="your-auth-token")

payload = {"alert_id": "live_alert_id","user_id": "live_user_id","transaction_id": "live_transaction_id","payloads": {"EMAIL": {"recipient":"example@example.com","personalized_attributes": {"attr": "value"}}}}
response = client.send(payload)
print(response)
```

### Using Basic Auth

#### Inform Test Client

```python
from moengage.inform.client.core.sandbox_client import SandBoxClient

client = SandBoxClient(username="your-user-name", password="your-pass-word")

payload = {"alert_id": "test_alert_id","user_id": "test_user_id","transaction_id": "test_transaction_id","payloads": {"SMS": {"recipient":"samplemobileno","personalized_attributes": {"attr": "value"}}}}
response = client.send(payload)
print(response)
```

#### Inform Live Client

```python
from moengage.inform.client.core.inform_client import InformClient

client = InformClient(username="your-user-name", password="your-pass-word")

payload = {"alert_id": "live_alert_id","user_id": "live_user_id","transaction_id": "live_transaction_id","payloads": {"EMAIL": {"recipient":"example@example.com","personalized_attributes": {"attr": "value"}}}}
response = client.send(payload)
print(response)
```

If you need to use a base url other than the default https://sandbox-inform-api-00.moengage.com/v1 for test Inform API, you can pass it as a parameter to the SandBoxClient:
```python
client = SandBoxClient(base_url="your-base-url", username="your-user-name", password="your-pass-word")
```
If you need to use a base url other than the default https://inform-api-00.moengage.com/v1 for live Inform API, you can pass it as a parameter to the InformClient:
```python
client = InformClient(base_url="your-base-url", username="your-user-name", password="your-pass-word")
```

## APIs

For a full description of request and response payloads and properties, please see the [official Inform API docs](https://help.moengage.com/hc/en-us/articles/10672957787284-Overview-Inform).

### Inform Test API

- `send(requestbody) (response, error)` [[?]](https://www.postman.com/moengage-dev/workspace/api-docs/request/3182294-dce6282f-4e49-4f69-9dd4-1d531c286744)

### Inform Send API

- `send(requestbody) (response, error)` [[?]](https://www.postman.com/moengage-dev/workspace/api-docs/request/3182294-47c54026-a3fd-4c7a-9480-504665f03228)

