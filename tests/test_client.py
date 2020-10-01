from azure_databricks_sdk_python import Client, AuthMethods
from azure_databricks_sdk_python.client import AzureADUserClient, AzureADServicePrincipalClient, PersonalAccessTokenClient

import pytest

from .helpers import create_client
client = create_client()

def test_client_using_azure_ad_user():
    assert isinstance(Client(auth_method=AuthMethods.AZURE_AD_USER,
                             databricks_instance="ddd", access_token="ddd"), AzureADUserClient)

def test_client_using_azure_ad_user_non_admin_as_admin():
    assert isinstance(Client(auth_method=AuthMethods.AZURE_AD_USER,
                             databricks_instance="ddd", access_token="ddd", resource_id="hello"), AzureADUserClient)

def test_client_using_azure_ad_service_principal():
    assert isinstance(Client(auth_method=AuthMethods.AZURE_AD_SERVICE_PRINCIPAL,
                             databricks_instance="ddd", access_token="ddd", management_token="ddd", resource_id="ddd"), AzureADServicePrincipalClient)


def test_client_using_azure_ad_service_principal_non_admin():
    assert isinstance(Client(auth_method=AuthMethods.AZURE_AD_SERVICE_PRINCIPAL,
                             databricks_instance="ddd", access_token="ddd"), AzureADServicePrincipalClient)


def test_client_using_personal_access_token():
    assert isinstance(Client(databricks_instance="ddd",
                             personal_access_token="ddd"), PersonalAccessTokenClient)


def test_bad_client_test_connection():
    assert Client(databricks_instance="ddd",
                             personal_access_token="ddd").test_connection() == False

def test_good_client_test_connection():
    assert client.test_connection() == True



def test_wrong_auth_method():
    with pytest.raises(Exception):
        Client(auth_method="jwt", databricks_instance="ddd", access_token="ddd")
