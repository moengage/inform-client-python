# `inform-client-python`

This Python Package helps you send notifications through [MoEngage Inform](https://www.moengage.com/blog/introducing-transactional-alerts-moengage-inform/), the smartest way to design &amp; deliver notifications. Design your notifications and then deliver to any channel through one API. Currently Email and SMS channels are supported.


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
