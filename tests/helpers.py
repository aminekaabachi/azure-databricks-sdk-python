from environs import Env
from azure_databricks_sdk_python import Client

env = Env()
env.read_env()

def create_client():
    token = env.str("PERSONAL_ACCESS_TOKEN")
    instance = env.str("DATABRICKS_INSTANCE")

    return Client(databricks_instance=instance,  personal_access_token=token)

def create_bad_client():
    env = Env()
    env.read_env()

    instance = env.str("DATABRICKS_INSTANCE")

    return Client(databricks_instance=instance,  personal_access_token="wrong")