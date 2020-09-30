from azure_databricks_sdk_python.types import AuthMethods
from azure_databricks_sdk_python.tokens import Tokens
from azure_databricks_sdk_python.clusters import Clusters


# Current API version
API_VERSION = 2.0

class Composer:
    """ Composer that aggregates API wrappers.
    """
    def compose(self, args):
        """composes self with API wrappers.

        Args:
            args (dict): configuration dict.

        Returns:
            Composer: return new composed object.
        """
        self.tokens = Tokens(**args)
        self.clusters = Clusters(**args)
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
        using a partial config dictionary

        Args:
            instance (String): Databricks instance name (FQDN).
            config (dict): Contains partial connection information.

        Returns:
            dict: dictionary with all connection information.
        """

        version = API_VERSION
        base_url = 'https://{instance}/api/{version}/'.format(
            instance=instance, version=version)
        return {**{'version': version, 'base_url': base_url}, **config}

    def __getattr__(self, attr):
        """Implementing a composition with the self._composed object
           hence Client().foo with now return self._composed().foo
        """
        return getattr(self._composed, attr)


class PersonalAccessTokenClient(BaseClient):
    """Client that authentificates using PERSONAL_ACCESS_TOKEN method"""

    def __init__(self, databricks_instance: str, personal_access_token: str):
        """Initializing the client with a personal access token

        Args:
            databricks_instance (str): Databricks instance name (FQDN).
            personal_access_token (str): Databricks personal access token.
        """
        config = self._setup_config(personal_access_token)
        super().__init__(databricks_instance, Composer(), config)

    def _setup_config(self, personal_access_token: str):
        """Generates partial config

        Args:
            personal_access_token (str): Databricks personal access token.

        Returns:
            dict: partial config.
        """
        return {'auth_method': AuthMethods.PERSONAL_ACCESS_TOKEN,
                'personal_access_token': personal_access_token}


class AzureADUserClient(BaseClient):
    """Client that authentificates using AZURE_AD_USER method"""

    def __init__(self, databricks_instance: str, access_token: str, resource_id: str = None):
        """Initializing the client with an access token and a resource_id

        Args:
            databricks_instance (str): Databricks instance name (FQDN).
            access_token (str): Azure AD access token.
            resource_id (str, optional): Databricks workspace resource ID. 
            check _setup_config for details. Defaults to None.
        """
        config = self._setup_config(access_token, resource_id)
        super().__init__(databricks_instance, Composer(), config)

    def _setup_config(self, access_token: str, resource_id: str):
        """Generates partial config

        Args:
            access_token (str): Azure AD access token.
            resource_id (str): Required for non-admin users who want to log in as an admin user.
            User must be in a Contributor or Owner role on the workspace resource in Azure.
        Returns:
            dict: partial config.
        """

        config = {}
        if (resource_id):
            config = {'resource_id': resource_id}
        return {**{'auth_method': AuthMethods.AZURE_AD_USER,
                   'access_token': access_token}, **config}


class AzureADServicePrincipalClient(BaseClient):
    """Client that authentificates using AZURE_AD_SERVICE_PRINCIPAL method"""

    def __init__(self, databricks_instance: str, access_token: str, management_token: str = None, resource_id: str = None):
        """Initializing the client with an access token, management token, and a resource_id

        Args:
            databricks_instance (str): Databricks instance name (FQDN).
            access_token (str): Azure AD access token.
            management_token (str, optional):  Azure AD management token.
            resource_id (str, optional): Databricks workspace resource ID. 
            check _setup_config for details. Defaults to None.
        """
        config = self._setup_config(
            access_token, management_token, resource_id)
        super().__init__(databricks_instance, Composer(), config)

    def _setup_config(self, access_token: str, management_token: str, resource_id: str):
        """Generates partial config

        Args:
            access_token (str): Azure AD access token.
            management_token (str): Azure AD management token.
            resource_id (str):  Databricks workspace resource ID. 
            Required only for admin sp. Check [*] for non-admin sp.

        Returns:
            dict: partial config.
        """
        config = {}

        if (resource_id):
            config = {'resource_id': resource_id,
                      'management_token': management_token}
        else:
            """[*] : Non-admin service principal authentification:
            Prior to this login, the service principal must be added to the workspace
            either as part of the admin user login or using the Add service principal
            endpoint (via SCIM API).
            """
            pass

        return {**{'auth_method': AuthMethods.AZURE_AD_SERVICE_PRINCIPAL,
                   'access_token': access_token}, **config}


class Client:
    """Factory for Clients"""
    def __new__(cls, auth_method=AuthMethods.PERSONAL_ACCESS_TOKEN, **kargs):
        """Return a client based on auth_method

        Args:
            auth_method (AuthMethods, optional): authentification method. Defaults to AuthMethods.PERSONAL_ACCESS_TOKEN.
        """
        def auth_method_error(_): return (_ for _ in ()).throw(
            Exception('Authentification method not defined.'))

        methods = {
            AuthMethods.PERSONAL_ACCESS_TOKEN: cls.use_personal_access_token,
            AuthMethods.AZURE_AD_USER: cls.use_azure_ad_user,
            AuthMethods.AZURE_AD_SERVICE_PRINCIPAL: cls.use_azure_ad_service_principal
        }

        return methods.get(auth_method, auth_method_error)(**kargs)

    @staticmethod
    def use_personal_access_token(databricks_instance: str, personal_access_token: str):
        """Returns a personal_access_token client

        Args:
            databricks_instance (str): Databricks instance name (FQDN).
            personal_access_token (str): Databricks personal access token.

        Returns:
            PersonalAccessTokenClient: personal_access_token client.
        """
        return PersonalAccessTokenClient(databricks_instance, personal_access_token)

    @staticmethod
    def use_azure_ad_user(databricks_instance: str, access_token: str, resource_id: str = None):
        """Returns a azure_ad_user client

        Args:
            databricks_instance (str): Databricks instance name (FQDN).
            access_token (str): Azure AD access token.
            resource_id (str, optional): Databricks workspace resource ID. Defaults to None.
            Required for non-admin users who want to log in as an admin user.

        Returns:
            AzureADUserClient: azure_ad_user client.
        """
        return AzureADUserClient(databricks_instance, access_token, resource_id)

    @staticmethod
    def use_azure_ad_service_principal(databricks_instance: str, access_token: str, management_token: str = None, resource_id: str = None):
        """Returns a azure_ad_service_principal client

        Args:
            databricks_instance (str): Databricks instance name (FQDN).
            access_token (str): Azure AD access token.
            management_token (str): Azure AD management token. Defaults to None.
            resource_id (str, optional): Databricks workspace resource ID. Defaults to None.
            Required only for admin sp. For non-admin, Service principal must
            be added to the workspace prior to login.

        Returns:
            AzureADServicePrincipalClient: azure_ad_service_principal client.
        """
        return AzureADServicePrincipalClient(databricks_instance, access_token, management_token, resource_id)
