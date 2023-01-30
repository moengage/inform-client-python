# `moe-inform-client`

## Table of contents

- Overview
- Installation
- Requirements
- Usage
- Troubleshooting and FAQs
- APIs
- Contributing
- License

## Overview

This Python Package helps you in sending notifications through [MoEngage Inform](https://www.moengage.com/blog/introducing-transactional-alerts-moengage-inform/), the smartest way to design &amp; deliver notifications. Deliver your transactional messages to any channel through one API. Currently Email and SMS channels are supported.
For an official overview of Inform Product, please see the [Inform Overview](https://help.moengage.com/hc/en-us/articles/10672957787284-Overview-Inform) or contact us at [MoEngage](https://moengage.com/). Happy engaging your users!

## Installation
Install from PyPI using [pip](http://www.pip-installer.org/en/latest/):

```shell
$ pip install moe-inform-client
```

python3.9 or later is required.

## Requirements
```text
  StrEnum~=0.4.9
  urllib3~=1.26.13
  jsonschema~=4.17.3
```
Note: Install these individually if any issue raises in installation of these requirements like this 
```shell
$ pip install StrEnum~=0.4.9
```

## Usage

```python
from informclient import InformClient
"""
base_url = "https://sandbox-inform-api-XX.moengage.com"
app_id = "XXXXXXXXXX"
api_secret = "XXXXXXXXXX"
"""
client = InformClient(base_url, app_id, api_secret)
payload = {
    "alert_id": "XXXXXXXXXX",
    "user_id": "XXXXXXXXXX",
    "transaction_id": "XXXXXXXXXX",
    "payloads": 
        {
            "SMS": 
                {
                    "recipient":"+91XXXXXXXXXX",
                    "personalized_attributes": {
                        "attr": "value"
                    }
                },
            "EMAIL":
                {
                    "recipient":"XXXXXXXXXX@example.com",
                    "personalized_attributes": {
                        "attr": "value"
                    }
                }
        }
}
response = client.send_alert(payload)
print(response)
```

## Troubleshooting and FAQs
- ### What is the format of base_url?
    - The base_url should be of the format "https://sandbox-inform-api-XX.moengage.com"
    
- ### Why do I get **sslcertverificationerror** while sending an alert? 
    - Inform Client is only supported through secured HTTPS connection requests. If the request throws
      **sslcertverificationerror**. Run the following commands.
        - For **MacOSx**
            ```shell
            $ pip install certifi
            $ /Applications/Python\ 3.9/Install\ Certificates.command
            ```
        - For **Windows**
            ```shell
            $ pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org informclient
            ```
 

## APIs

For a full description of request and response payloads and properties, please see the [Official Inform API docs](https://developers.moengage.com/hc/en-us/articles/10699624590868).

- `send_alert(requestbody) (response, Error)` [[See alert Description ]](https://help.moengage.com/hc/en-us/articles/10717041310484-Test-Alert#attributes-0-5)

## Contributing

Bug reports and pull requests are welcome on GitHub at https://github.com/moengage/inform-client-python. See [CONTRIBUTING.md](CONTRIBUTING.md) for more info.

## License

This package is available as open source under the terms of the [MIT License](https://opensource.org/licenses/MIT).
