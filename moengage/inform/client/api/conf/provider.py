import json


class InformClientConfigProvider(object):

    def __init__(self):
        super().__init__()

    def get_test_base_url(self):
        f = open("moengage/inform/client/api/conf/config.json", "r")
        data = json.loads(f.read())
        f.close()
        return data['test_base_url']

    def get_live_base_url(self):
        f = open("moengage/inform/client/api/conf/config.json", "r")
        data = json.loads(f.read())
        f.close()
        return data['live_base_url']