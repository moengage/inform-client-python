from mongoengine import *


class ChannelPayload(EmbeddedDocument):
    recipient = StringField(required=True, min_length=1, max_length=50, allow_empty=False)
    personalized_attributes = DictField(key_validator=StringField(), value_validator=StringField(), default={})


class TestSentRequest(Document):
    alert_id = ObjectIdField(required=True)
    user_id = StringField(default=None)
    transaction_id = StringField(min_length=1, max_length=50, required=True)
    payloads = DictField(required=True, key_validator=StringField(choices=['EMAIL', 'SMS']),
                         value_validator=EmbeddedDocumentField(ChannelPayload))


class SentRequest(Document):
    inform_id = ObjectIdField(required=True)
    user_id = StringField(default=None)
    transaction_id = StringField(min_length=1, max_length=50, required=True)
    payloads = DictField(required=True, key_validator=StringField(choices=['EMAIL', 'SMS']),
                         value_validator=EmbeddedDocumentField(ChannelPayload))
