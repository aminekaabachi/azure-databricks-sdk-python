from azure_databricks_sdk_python.api import API
from azure_databricks_sdk_python.types.tokens import PublicTokenInfo


class Tokens(API):
    """The Token API allows you to create, list, and revoke tokens
    that can be used to authenticate and access Azure Databricks REST APIs.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def list(self):
        """List all the valid tokens for a user-workspace pair.

        Returns:
            [PublicTokenInfo]: A list of token information for a user-workspace pair.
        """
        endpoint = '/token/list'
        res = self._get(endpoint)
        if res.status_code == 200:
            return [PublicTokenInfo(**token) for token in res.json().get('token_infos')]
        else:
            self._handle_error(res)

    def create(self, comment: str = None, lifetime_seconds: int = 7776000):
        """Createsand return a token. 

        Args:
            comment (str, optional): Optional description to attach to the token. 
            Defaults to None.
            lifetime_seconds (int, optional): The lifetime of the token, in seconds. 
            If no lifetime is specified, the token remains valid indefinitely.
            Defaults to 7776000 (90j).

        Returns:
            dict: contains token_value and token_info as a PublicTokenInfo.
        """
        endpoint = '/token/create'
        data = {'lifetime_seconds': lifetime_seconds,
                'comment': comment}
        res = self._post(endpoint, data)
        if res.status_code == 200:
            return {'token_value': res.json().get('token_value'),
                    'token_info': PublicTokenInfo(**res.json().get('token_info'))}
        else:
            self._handle_error(res)

    def delete(self, token_id: str):
        """Revoke an access token. 

        Args:
            token_id (str): The ID of the token to be revoked.

        Returns:
            Boolean: In case of success or will raise an exception.
        """
        endpoint = '/token/delete'
        data = {'token_id': token_id}
        res = self._post(endpoint, data)
        if res.status_code == 200:
            return True
        else:
            self._handle_error(res)
