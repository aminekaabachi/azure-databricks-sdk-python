import json
import requests

from azure_databricks_sdk_python.types import AuthMethods


class API:
    def __init__(self, **kwargs):
        auth_method = kwargs.pop('auth_method')
        base_url = kwargs.pop('base_url')

        if (auth_method == AuthMethods.PERSONAL_ACCESS_TOKEN):
            token = kwargs.pop('personal_access_token')
            self._dispatcher = APIWithPersonalAccessToken(
                base_url, token)

        elif (auth_method == AuthMethods.AZURE_AD_USER):
            access_token = kwargs.pop('access_token')
            resource_id = kwargs.pop('resource_id', None)
            self._dispatcher = APIWithAzureADUser(
                 base_url, access_token, resource_id)

        elif (auth_method == AuthMethods.AZURE_AD_SERVICE_PRINCIPAL):
            access_token = kwargs.pop('access_token')
            resource_id = kwargs.pop('resource_id', None)
            management_token = kwargs.pop('management_token', None)
            self._dispatcher = APIWithAzureADServicePrincipal(
                base_url, access_token, management_token, resource_id)

        else:
            raise Exception('Authentification method not defined.')

    def __getattr__(self, attr):
        return getattr(self._dispatcher, attr)


class APIWithAuth:
    def _get(self, endpoint, data=None):
        if endpoint.startswith('/'):
            endpoint = endpoint[1:]
        url = self._base_url + endpoint
        return requests.get(url=url, headers=self._headers, json=data)

    def _post(self, endpoint, data):
        if endpoint.startswith('/'):
            endpoint = endpoint[1:]

        data_json = json.dumps(data, ensure_ascii=False)

        url = self._base_url + endpoint
        return requests.post(url=url, headers=self._headers, data=data_json)


class APIWithPersonalAccessToken(APIWithAuth):
    def __init__(self, base_url, personal_access_token):
        self._base_url = base_url
        self._token = personal_access_token
        self._headers = {'Authorization': 'Bearer {0}'.format(self._token)}


class APIWithAzureADUser(APIWithAuth):
    def __init__(self, base_url, access_token, resource_id):
        self._base_url = base_url
        self._token = access_token
        self._resource_id = resource_id
        self._headers = {'Authorization': 'Bearer {0}'.format(
            self._token)}
        if (resource_id):
            self._headers = {
                'X-Databricks-Azure-Workspace-Resource-Id': self._resource_id, 
                **self._headers}


class APIWithAzureADServicePrincipal(APIWithAuth):
    def __init__(self, base_url, access_token, management_token, resource_id):
        self._base_url = base_url
        self._token = access_token
        self._resource_id = resource_id
        self._management_token = management_token
        self._headers = {'Authorization': 'Bearer {0}'.format(
            self._token)}
        if (resource_id):
            self._headers = {
                'X-Databricks-Azure-Workspace-Resource-Id': self._resource_id,
                'X-Databricks-Azure-SP-Management-Token': self._management_token,
                **self._headers}
