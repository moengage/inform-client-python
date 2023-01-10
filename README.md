# `inform-client-python`

This Python Package helps you send notifications through [MoEngage Inform](https://www.moengage.com/blog/introducing-transactional-alerts-moengage-inform/), the smartest way to design &amp; deliver notifications. Deliver your transactional messages to any channel through one API. Currently Email and SMS channels are supported.

APIs supported:

- Inform Test API - Sandbox API
- Inform Send API - Live API

## Official Inform API docs

For a full description of request and response payloads and properties, please see the [official Inform API docs](https://help.moengage.com/hc/en-us/articles/10672957787284-Overview-Inform).

## Installation
Install from PyPI using pip:

```
$ pip install inform-client-python
```
python3.X is required.

## Usage


#### Inform  Client

```python
from moengage.inform.client.core.inform_client import InformClient
client = InformClient(base_url, app_id, api_secret)
payload = {"alert_id": "alert_id","user_id": "user_id","transaction_id": "transaction_id","payloads": {"SMS": {"recipient":"samplemobileno","personalized_attributes": {"attr": "value"}}}}
response = client.send_alert(payload)
print(response)
```


## APIs

For a full description of request and response payloads and properties, please see the [official Inform API docs](https://help.moengage.com/hc/en-us/articles/10672957787284-Overview-Inform).

### Inform Test API - Sandbox API

- `send_alert(requestbody) (response, Error)` [[Postman API Description]](https://www.postman.com/moengage-dev/workspace/api-docs/request/3182294-dce6282f-4e49-4f69-9dd4-1d531c286744)

### Inform Send API - Live API

- `send_alert(requestbody) (response, Error)` [[Postman API Description]](https://www.postman.com/moengage-dev/workspace/api-docs/request/3182294-47c54026-a3fd-4c7a-9480-504665f03228)

