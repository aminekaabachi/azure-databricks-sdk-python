from azure_databricks_sdk_python import Client, AuthMethods
from azure_databricks_sdk_python.api import API
from azure_databricks_sdk_python.tokens import Tokens

def test():
    api = API(auth_method=AuthMethods.PERSONAL_ACCESS_TOKEN,
        databricks_instance="ddd", base_url="http://google.com/", personal_access_token="ddd")

    Tokens(auth_method=AuthMethods.AZURE_AD_USER,
        databricks_instance="ddd", base_url="http://google.com/", access_token="ddd", resource_id="/dd/ddd/dd/").create()

    Tokens(auth_method=AuthMethods.AZURE_AD_SERVICE_PRINCIPAL,
        databricks_instance="ddd", base_url="http://google.com/", access_token="ddd").create()


    client = Client(databricks_instance="ddd", personal_access_token="ddd")

    client.tokens.create()

    assert False