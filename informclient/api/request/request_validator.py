import json
from jsonschema import RefResolver, Draft7Validator


def validate_request(request_body):
    channelpayload = {
        "$id": "/schemas/channelpayload",
        "type": "object",
        "properties": {
            "recipient": {"type": "string", "minLength": 1, "maxLength": 100},
            "personalized_attributes": {"type": "object"}
        },
        "required": ["recipient"]
    }
    payloads = {
        "$id": "/schemas/payloads",
        "type": "object",
        "propertyNames": {
            "enum": [
                "EMAIL",
                "SMS"
            ]
        },
        "patternProperties": {
            "": {
                "$ref": "/schemas/channelpayload"
            }
        },
        "minProperties": 1
    }
    request = {
        "$id": "/schemas/request",
        "type": "object",
        "properties": {
            "alert_id": {
                "type": "string",
                "minLength": 24,
                "maxLength": 24,
                "pattern": "^[A-Fa-f0-9]{24}$"
            },
            "user_id": {"type": "string"},
            "transaction_id": {
                "type": "string",
                "minLength": 1,
                "maxLength": 50
            },
            "payloads": {"$ref": "/schemas/payloads"}
        },
        "required": ["alert_id", "transaction_id", "payloads"]
    }
    channelpayload_schema = json.loads(json.dumps(channelpayload))
    payloads_schema = json.loads(json.dumps(payloads))
    request_schema = json.loads(json.dumps(request))
    schema_store = {
        channelpayload_schema['$id']: channelpayload_schema,
        payloads_schema['$id']: payloads_schema,
        request_schema['$id']: request_schema,
    }
    resolver = RefResolver.from_schema(request_schema, store=schema_store)
    validator = Draft7Validator(request_schema, resolver=resolver)
    validator.validate(request_body)
