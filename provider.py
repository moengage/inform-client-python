import os

import json


class InformClientConfigProvider(object):

    def __init__(self):
        self.current_dir = os.path.dirname(os.path.abspath('config.json'))
        self.file = os.path.join(self.current_dir, 'config.json')
        with open(self.file, 'r', encoding='utf-8') as f:
            self.data = json.load(f)

    def get_test_base_url(self):
        return self.data['test_base_url']

    def get_live_base_url(self):
        return self.data['live_base_url']