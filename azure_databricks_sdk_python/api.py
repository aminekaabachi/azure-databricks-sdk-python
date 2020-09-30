import json
import requests
import urllib.parse
from cattr import structure, unstructure

from azure_databricks_sdk_python.types import AuthMethods


class API:
    """Base class for API wrappers.
    It composes with APIWithAuth API classes.
    """

    def __init__(self, **kwargs):
        """takes keyword arguements and constructs a dispatcher
        as an instance of APIWithAuth that will act as this class
        via composition.

        Raises:
            Exception: In case the auth method is not recognised.
        """
        auth_method = kwargs.pop('auth_method')
        base_url = kwargs.pop('base_url')
        print(base_url)
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
        """Implementing a composition with the self._dispatcher object
        hence API().foo with now return self._dispatcher().foo
        """
        return getattr(self._dispatcher, attr)


class APIWithAuth:
    """Base class API composers
    the API composers implement auth specific logic
    as they inherit from this class that implements
    common functionality such as http get and post
    and also error handeling.
    """

    def _get(self, endpoint: str, data=None):
        """Performs a http get to BASE_URL/endpoint 
        with data passed as json body

        Args:
            endpoint (str): API endpoint
            data (dict, optional): parameters to send to the API endpoint. Defaults to None.

        Returns:
            Response: the response object from http call.
        """
        url = urllib.parse.urljoin(self._base_url, endpoint.lstrip('/'))
        print(url)
        return requests.get(url=url, headers=self._headers, json=data)

    def _post(self, endpoint: str, data=None):
        """Performs a http post to BASE_URL/endpoint 
        with data passed as body

        Args:
            endpoint (str): API endpoint
            data (dict, optional): parameters to send to the API endpoint. Defaults to None.

        Returns:
            Response: the response object from http call.
        """
        data_json = json.dumps(data, ensure_ascii=False)
        url = self._base_url + endpoint
        url = urllib.parse.urljoin(self._base_url, endpoint.lstrip('/'))
        return requests.post(url=url, headers=self._headers, data=data_json)

    def _handle_error(self, res):
        """Helper method to handle http errors

        Args:
            res (Response): the response object from http call.

        Raises:
            Exception: In case of authorization error.
            Exception: For all other cases.
        """

        # TODO: Implement proper error handling.

        if res.status_code == 403:
            raise Exception("Not authorized or invalid token.")
        else:
            raise Exception("Response code {0}: {1} {2}".format(res.status_code,
                                                                res.json().get('error_code'),
                                                                res.json().get('message')))

    def _safe_handle(self, res, value, type=None):
        """Helper method to safely handle http response

        Args:
            res (Response): http response.
            value (any): value to return.

        Returns:
            any: the returned object. Raise exception if code is not 200.
        """
        
        if res.status_code == 200:
            if type:
                return structure(value, type)
            else:
                return value
        else:
            self._handle_error(res)

    def _validate(self, req, type, validate=True):
        """Validates users input to be passed to api

        Args:
            req (object): user input.
            type (object): the type to be validated against.
            validate (bool): to validate or not the input against the type.

        Raises:
            ValueError: if validates=True, Raises in case the input is not type serializable.
            ValueError: if validates=True,Raises in case the input is not a dict.

        Returns:
            dict: the input data in dict format.
        """
        data = req

        if validate:
            print(type)
            if not isinstance(req, type):
                try:
                    data = structure(req, type)
                except Exception as err:
                    raise ValueError(
                        'Request is a valid {0}: {1}'.format(type.__name__, err))
            return unstructure(data)
        else:
            if not isinstance(req, dict):
                raise ValueError(
                    'Request is not a dict. {0} passed instead.'.format(req))
            return data


class APIWithPersonalAccessToken(APIWithAuth):
    """API composers for PersonalAccessToken auth"""

    def __init__(self, base_url: str, personal_access_token: str):
        """Sets up request parameters for 
        the personal access token auth method.

        Args:
            base_url (str): Databricks API url.
            personal_access_token (str): Databricks personal access token.
        """
        self._base_url = base_url
        self._token = personal_access_token
        self._headers = {'Authorization': 'Bearer {0}'.format(self._token)}


class APIWithAzureADUser(APIWithAuth):
    """API composers for AzureADUser auth"""

    def __init__(self, base_url: str, access_token: str, resource_id: str):
        """Sets up request parameters for 
        the personal Azure AD user auth method.

        Args:
            base_url (str): Databricks API url.
            access_token (str): Azure AD access token.
            resource_id (str): Databricks workspace resource ID.
        """
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
    """API composers for AzureADServicePrincipal auth"""

    def __init__(self, base_url: str, access_token: str, management_token: str, resource_id: str):
        """Sets up request parameters for 
        the personal Azure AD service principal auth method.

        Args:
            base_url (str): Databricks API url.
            access_token (str): Azure AD access token.
            management_token (str): AD management token.
            resource_id (str): Databricks workspace resource ID.
        """
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
