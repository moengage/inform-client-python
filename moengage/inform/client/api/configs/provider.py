import os

import json


class InformClientConfigProvider(object):

    def __init__(self):
        self.file = os.path.join('moengage/inform/client/api/configs/', 'config.json')
        if not os.path.isfile(self.file):
            raise FileNotFoundError("config.json is not present. Please provide base_url")
        else:
            with open(self.file, 'r', encoding='utf-8') as f:
                self.data = json.load(f)

    def get_test_base_url(self):
        return self.data['test_base_url']

    def get_live_base_url(self):
        return self.data['live_base_url']