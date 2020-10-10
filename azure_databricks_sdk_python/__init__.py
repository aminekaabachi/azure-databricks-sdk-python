from azure_databricks_sdk_python.client import Client
from azure_databricks_sdk_python.types.auth_methods import AuthMethods
import logging

__VERSION__ = '0.0.2'

# Set default logging handler to avoid "No handler found" warnings.
import logging
from logging import NullHandler

logging.getLogger(__name__).addHandler(NullHandler())