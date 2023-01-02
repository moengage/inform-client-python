import os

import json
from jsonschema import RefResolver, Draft7Validator


def validate_request(request_body):
    schemas_dir = 'moengage/inform/client/api/request/schemas/'
    with open(os.path.join(schemas_dir, 'schema-channelpayload.json'), 'r') as f:
        channelpayload = f.read()
    with open(os.path.join(schemas_dir, 'schema-payload.json'), 'r') as f:
        payloads = f.read()
    with open(os.path.join(schemas_dir, 'schema-request.json'), 'r') as f:
        request = f.read()
    channelpayload_schema = json.loads(str(channelpayload).replace("\'", "\""))
    payloads_schema = json.loads(str(payloads).replace("\'", "\""))
    request_schema = json.loads(str(request).replace("\'", "\""))
    schema_store = {
        channelpayload_schema['$id']: channelpayload_schema,
        payloads_schema['$id']: payloads_schema,
        request_schema['$id']: request_schema,
    }
    resolver = RefResolver.from_schema(request_schema, store=schema_store)
    validator = Draft7Validator(request_schema, resolver=resolver)
    request_body = json.loads(str(request_body).replace("\'", "\""))
    validator.validate(request_body)
