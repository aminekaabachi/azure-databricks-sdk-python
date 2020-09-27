
from enum import Enum

class AuthMethod(Enum):
    PERSONAL_ACCESS_TOKEN = 'personal_access_token'
    AZURE_AD_USER = 'azure_ad_user'
    AZURE_AD_SERVICE_PRINCIPAL = 'azure_ad_service_principal'

class BaseClient:

    """ Base for API Clients """

    def __init__(self, databricks_instance, config={}):
        """Initializing the base class for API Clients

        Args:
            databricks_instance (String): Databricks instance name (FQDN).
            config (dict, optional): Contains connection 
            parameters and useful information. Defaults to {}.
        """
        self._version = '2.0'
        self._instance = databricks_instance
        self._base_url = 'https://{instance}/api/{version}'.format(instance=self._instance, version=self._version)
        self._config = {**{'version': self._version, 'base_url': self._base_url}, **config}
        
        print(self._config)


class PersonalAccessTokenClient(BaseClient):

    def __init__(self, databricks_instance, personal_access_token):
        config = {'auth_method': AuthMethod.PERSONAL_ACCESS_TOKEN, 'token': personal_access_token}
        super().__init__(databricks_instance, config)

class AzureADUserClient(BaseClient):

    def __init__(self, databricks_instance, access_token, resource_id=None):

        config = {}

        # Required for non-admin users who want to log in as an admin user
        # User must be in a Contributor or Owner role on the workspace resource in Azure
        if (resource_id):
            config = {'resource_id': resource_id}
        
        config = {**{'auth_method': AuthMethod.AZURE_AD_USER, 'access_token': access_token}, **config}
        super().__init__(databricks_instance, config)


class AzureADServicePrincipalClient(BaseClient):

     def __init__(self, databricks_instance, access_token, management_token=None, resource_id=None):

        config = {}

        if (resource_id):
            config = {'resource_id': resource_id, 'management_token': management_token}
        else:
            # Non-admin service principal authentification:
            # Prior to this login, the service principal must be added to the workspace
            # either as part of the admin user login or using the Add service principal
            # endpoint (via SCIM API).
            pass

        config = {**{'auth_method': AuthMethod.AZURE_AD_SERVICE_PRINCIPAL, 'access_token': access_token}, **config}
        super().__init__(databricks_instance, config)


class Client:
    
    def __new__(self, auth_method=AuthMethod.PERSONAL_ACCESS_TOKEN, **kargs):
        if (auth_method == AuthMethod.PERSONAL_ACCESS_TOKEN):
            return self.use_personal_access_token(**kargs)
        elif (auth_method == AuthMethod.AZURE_AD_USER):
            return self.use_azure_ad_user(**kargs)
        elif (auth_method == AuthMethod.AZURE_AD_SERVICE_PRINCIPAL):
            return self.use_azure_ad_service_principal(**kargs)
        else:
            raise Exception('Authentification method is not defined.')

    @staticmethod
    def use_personal_access_token(databricks_instance, personal_access_token):
        return PersonalAccessTokenClient(databricks_instance, personal_access_token)
    
    @staticmethod
    def use_azure_ad_user(databricks_instance, access_token, resource_id=None):
        return AzureADUserClient(databricks_instance, access_token, resource_id)
    
    @staticmethod
    def use_azure_ad_service_principal(databricks_instance, access_token, management_token, resource_id=None):
        return AzureADServicePrincipalClient(databricks_instance, access_token, management_token, resource_id)