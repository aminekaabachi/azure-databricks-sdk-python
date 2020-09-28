from azure_databricks_sdk_python.api import API

class Tokens(API):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def create(self, comment="", lifetime_seconds=7776000):
        endpoint = '/token/create'

        data = {'lifetime_seconds': lifetime_seconds,
                'comment': comment}

        res = self._get(endpoint, data)

        print(res.request.headers)