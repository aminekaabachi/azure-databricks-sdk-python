
class BaseClient:

    def __init__(self, databricks_instance, config={}):
        self._version = '2.0'
        self._instance = databricks_instance
        self._base_url = 'https://{instance}/api/{version}'.format(instance=self._instance, version=self._version)
        self._config = {**{'version': self._version, 'base_url': self._base_url}, **config}
        
        print(self._config)


class PersonalAccessTokenClient(BaseClient):

    def __init__(self, databricks_instance, personal_access_token):
        config = {'auth_type': 'personal_access_token', 'token': personal_access_token}
        super().__init__(databricks_instance, config)

class AzureADUserClient(BaseClient):

    def __init__(self, databricks_instance, access_token, resource_id=None):

        config = {}

        # Required for non-admin users who want to log in as an admin user
        # User must be in a Contributor or Owner role on the workspace resource in Azure
        if (resource_id):
            config = {'resource_id': resource_id}
        
        config = {**{'auth_type': 'azure_ad_user', 'access_token': access_token}, **config}
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

        config = {**{'auth_type': 'azure_ad_service_principal', 'access_token': access_token}, **config}
        super().__init__(databricks_instance, config)


class Client:
    
    def __new__(self, auth_method="personal_access_token", **kargs):
        if (auth_method == "personal_access_token"):
            return self.use_personal_access_token(**kargs)
        elif (auth_method == "azure_ad_user"):
            return self.use_azure_ad_user(**kargs)
        elif (auth_method == "using_azure_ad_service_principal"):
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