from azure_databricks_sdk_python.api import API
from azure_databricks_sdk_python.types.tokens import PublicTokenInfo

class Tokens(API):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def list(self):
        endpoint = '/token/list'
        res = self._get(endpoint)
        if res.status_code == 200:
            return [PublicTokenInfo(**token) for token in res.json().get('token_infos')]
        else:
            self._handle_error(res)

    def create(self, comment=None, lifetime_seconds=7776000):
        endpoint = '/token/create'
        data = {'lifetime_seconds': lifetime_seconds,
                'comment': comment}
        res = self._post(endpoint, data)
        if res.status_code == 200:
            return {'token_value': res.json().get('token_value'), 
                    'token_info': PublicTokenInfo(**res.json().get('token_info'))}
        else:
            self._handle_error(res)
            

    def delete(self, token_id):
        endpoint = '/token/delete'
        data = {'token_id': token_id}
        res = self._post(endpoint, data)
        if res.status_code == 200:
            return True
        else:
            self._handle_error(res)