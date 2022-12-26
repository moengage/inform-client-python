from mongoengine import Document, ObjectIdField, StringField, DictField


# TODO Key validation is not supported for DictField in mongoengine.
class SandBoxClientSentRequest(Document):
    alert_id = ObjectIdField(required=True)
    user_id = StringField(default=None)
    transaction_id = StringField(min_length=1, max_length=50, required=True)
    payloads = DictField(required=True, default={})


# TODO Key validation is not supported for DictField in mongoengine.
class InformClientSentRequest(Document):
    alert_id = ObjectIdField(required=True)
    user_id = StringField(default=None)
    transaction_id = StringField(min_length=1, max_length=50, required=True)
    payloads = DictField(required=True, default={})
