from .helpers import create_client, create_bad_client, rand_name, create_premium_client
import pytest
from typing import List

from azure_databricks_sdk_python.client import PersonalAccessTokenClient
from azure_databricks_sdk_python.exceptions import *
from azure_databricks_sdk_python.types.secrets import *

client = create_client()
premium_client = create_premium_client()

def test_secret_scopes_list():
    list = client.secrets.scopes.list()
    assert isinstance(list, List)

def test_scopes_create_and_delete():
    length = len(client.secrets.scopes.list())
    name = rand_name(10)
    scope = client.secrets.scopes.create(scope=name, initial_manage_principal="users")
    client.secrets.scopes.delete(scope=name)
    assert length == len(client.secrets.scopes.list())


def test_secrets_create_and_delete():
    name = rand_name(10)
    key = rand_name(10)
    scope = client.secrets.scopes.create(scope=name, initial_manage_principal="users")
    assert len(client.secrets.list(scope=name)) == 0
    client.secrets.put(scope=name, key=key, string_value="yoyo")
    assert len(client.secrets.list(scope=name)) == 1
    client.secrets.delete(scope=name, key=key)
    assert len(client.secrets.list(scope=name)) == 0
    client.secrets.scopes.delete(scope=name)

def test_secret_acls_not_possible_standard():
    name = rand_name(10)
    scope = client.secrets.scopes.create(scope=name, initial_manage_principal="users")
    with pytest.raises(AuthorizationError):
        list = client.secrets.acls.list(scope=name)
    client.secrets.scopes.delete(scope=name)

def test_secret_acls_possible_premium():
    name = rand_name(10)
    premium_client.secrets.scopes.create(scope=name)
    list = premium_client.secrets.acls.list(scope=name)
    assert len(list) == 1
    premium_client.secrets.scopes.delete(scope=name)

def test_secret_acls_possible_premium():
    name = rand_name(10)
    premium_client.secrets.scopes.create(scope=name)
    list = premium_client.secrets.acls.list(scope=name)
    assert len(list) == 1
    premium_client.secrets.scopes.delete(scope=name)

def test_secret_acls_get_premium():
    name = rand_name(10)
    premium_client.secrets.scopes.create(scope=name, initial_manage_principal="users")
    acl = premium_client.secrets.acls.get(scope=name, principal="users")
    assert acl.permission == AclPermission.MANAGE
    premium_client.secrets.scopes.delete(scope=name)

def test_secret_acls_create_delete():
    name = rand_name(10)
    premium_client.secrets.scopes.create(scope=name, initial_manage_principal="users")
    acl = premium_client.secrets.acls.put(scope=name, principal="users", permission=AclPermission.WRITE)
    res = premium_client.secrets.acls.delete(scope=name, principal="users")
    assert res == True
    premium_client.secrets.scopes.delete(scope=name)
