from moengage.campaigns.inform.service.interface.response.request_type import RequestType
from moengage.orm.fields import StringField, EnumField
from moengage.orm.models.base import SimpleDocument


class InformSentResponse(SimpleDocument):
    message = StringField(required=True)
    request_id = StringField(required=True)
    request_type = EnumField(RequestType)
