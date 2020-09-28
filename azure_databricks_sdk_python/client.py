
from enum import Enum

API_VERSION = 2.0


class AuthMethod(Enum):
    """Enum representing authentification method

    For now there are three support auth method for the API:
    - PERSONAL_ACCESS_TOKEN: Databricks personal access tokens [1].
    - AZURE_AD_USER: Azure Active Directory access token [2].
    - AZURE_AD_SERVICE_PRINCIPAL: Active Directory token using a service principal [3].

    [1]: https://docs.microsoft.com/en-us/azure/databricks/dev-tools/api/latest/authentication
    [2]: https://docs.microsoft.com/en-us/azure/databricks/dev-tools/api/latest/aad/app-aad-token
    [3]: https://docs.microsoft.com/en-us/azure/databricks/dev-tools/api/latest/aad/service-prin-aad-token
    """
    PERSONAL_ACCESS_TOKEN = 'personal_access_token'
    AZURE_AD_USER = 'azure_ad_user'
    AZURE_AD_SERVICE_PRINCIPAL = 'azure_ad_service_principal'


class Composer:

    def compose(self, args):
        print(args)
        return self


class BaseClient:

    """ Base Class for API Clients """

    def __init__(self, databricks_instance: str, composer: Composer, config={}):
        """Initializing the base class for API Clients

        Args:
            databricks_instance (String): Databricks instance name (FQDN).
            config (dict, optional): Contains connection parameters and
            useful information. Defaults to {}.
        """

        self._config = self._setup_default_config(databricks_instance, config)
        self._composed = composer.compose(self._config)

    def _setup_default_config(self, instance: str, config: dict):
        """This method builds up a config dict containing connection information

        Args:
            instance (String): Databricks instance name (FQDN).
            config (dict): Contains partial connection information.

        Returns:
            dict: dictionary with all connection information.
        """

        version = API_VERSION
        base_url = 'https://{instance}/api/{version}'.format(
            instance=instance, version=version)
        return {**{'version': version, 'base_url': base_url}, **config}

    def __getattr__(self, attr):
        """Implementing a composition with the self._composed object
           hence Client.foo with now return self._composed.foo
        """
        return getattr(self._composed, attr)


class PersonalAccessTokenClient(BaseClient):

    def __init__(self, databricks_instance, personal_access_token):
        config = self._setup_config(personal_access_token)
        super().__init__(databricks_instance, Composer(), config)

    def _setup_config(self, personal_access_token):
        return {'auth_method': AuthMethod.PERSONAL_ACCESS_TOKEN,
                'token': personal_access_token}


class AzureADUserClient(BaseClient):

    def __init__(self, databricks_instance, access_token, resource_id=None):
        config = self._setup_config(access_token, resource_id)
        super().__init__(databricks_instance, Composer(), config)

    def _setup_config(self, access_token, resource_id):
        config = {}
        # Required for non-admin users who want to log in as an admin user
        # User must be in a Contributor or Owner role on the workspace resource in Azure
        if (resource_id):
            config = {'resource_id': resource_id}
        return {**{'auth_method': AuthMethod.AZURE_AD_USER,
                   'access_token': access_token}, **config}


class AzureADServicePrincipalClient(BaseClient):

    def __init__(self, databricks_instance, access_token, management_token=None, resource_id=None):
        config = self._setup_config(
            access_token, management_token, resource_id)
        super().__init__(databricks_instance, Composer(), config)

    def _setup_config(self, access_token, management_token, resource_id):
        config = {}

        if (resource_id):
            config = {'resource_id': resource_id,
                      'management_token': management_token}
        else:
            # Non-admin service principal authentification:
            # Prior to this login, the service principal must be added to the workspace
            # either as part of the admin user login or using the Add service principal
            # endpoint (via SCIM API).
            pass

        return {**{'auth_method': AuthMethod.AZURE_AD_SERVICE_PRINCIPAL,
                   'access_token': access_token}, **config}


class Client:

    def __new__(cls, auth_method=AuthMethod.PERSONAL_ACCESS_TOKEN, **kargs):
        def auth_method_error(_): return (_ for _ in ()).throw(
            Exception('Authentification method not defined.'))

        methods = {
            AuthMethod.PERSONAL_ACCESS_TOKEN: cls.use_personal_access_token,
            AuthMethod.AZURE_AD_USER: cls.use_azure_ad_user,
            AuthMethod.AZURE_AD_SERVICE_PRINCIPAL: cls.use_azure_ad_service_principal
        }

        return methods.get(auth_method, auth_method_error)(**kargs)

    @staticmethod
    def use_personal_access_token(databricks_instance, personal_access_token):
        return PersonalAccessTokenClient(databricks_instance, personal_access_token)

    @staticmethod
    def use_azure_ad_user(databricks_instance, access_token, resource_id=None):
        return AzureADUserClient(databricks_instance, access_token, resource_id)

    @staticmethod
    def use_azure_ad_service_principal(databricks_instance, access_token, management_token, resource_id=None):
        return AzureADServicePrincipalClient(databricks_instance, access_token, management_token, resource_id)