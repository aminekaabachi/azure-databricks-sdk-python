from environs import Env
from azure_databricks_sdk_python import Client

def create_client():
    env = Env()
    env.read_env()

    token = env.str("PERSONAL_ACCESS_TOKEN")
    instance = env.str("DATABRICKS_INSTANCE")

    return Client(databricks_instance=instance,  personal_access_token=token)