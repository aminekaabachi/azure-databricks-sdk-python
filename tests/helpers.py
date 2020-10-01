from environs import Env
from azure_databricks_sdk_python import Client

import random
import string

def rand_name(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

env = Env()
env.read_env()

def create_client():
    token = env.str("PERSONAL_ACCESS_TOKEN")
    instance = env.str("DATABRICKS_INSTANCE")

    return Client(databricks_instance=instance,  personal_access_token=token)

def create_premium_client():
    token = env.str("PERSONAL_ACCESS_TOKEN_PREMIUM")
    instance = env.str("DATABRICKS_INSTANCE_PREMIUM")

    return Client(databricks_instance=instance,  personal_access_token=token)

def create_bad_client():
    instance = env.str("DATABRICKS_INSTANCE")
    return Client(databricks_instance=instance,  personal_access_token="wrong")