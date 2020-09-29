
from enum import Enum
from collections import namedtuple

API_VERSION = 2.0

class AuthMethods(Enum):
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


PublicTokenInfo = namedtuple('PublicTokenInfo', ['token_id', 'creation_time', 'expiry_time', 'comment'])
