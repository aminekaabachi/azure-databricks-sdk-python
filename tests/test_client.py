from azure_databricks_sdk_python import Client, AuthMethod
from azure_databricks_sdk_python.client import AzureADUserClient, AzureADServicePrincipalClient, PersonalAccessTokenClient

def test_client_using_azure_ad_user():
    assert isinstance(Client(auth_method=AuthMethod.AZURE_AD_USER, databricks_instance="ddd", access_token="ddd"), AzureADUserClient)

def test_client_using_personal_access_token():
    assert isinstance(Client(databricks_instance="ddd", personal_access_token="ddd"), PersonalAccessTokenClient)
