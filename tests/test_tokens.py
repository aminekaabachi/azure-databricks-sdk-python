from .helpers import create_client, create_bad_client
import pytest
from typing import List
from azure_databricks_sdk_python.client import PersonalAccessTokenClient

client = create_client()


@pytest.mark.order2
def test_token_create_and_delete():
    length = len(client.tokens.list())
    token = client.tokens.create(lifetime_seconds=None)
    client.tokens.delete(token_id=token.token_info.token_id)
    assert length == len(client.tokens.list())

@pytest.mark.order1
def test_tokens_list():
    list = client.tokens.list()
    if isinstance(client, PersonalAccessTokenClient):
        assert len(list) > 0
    assert isinstance(list, List)


def test_token_creation_error():
    with pytest.raises(Exception):
        bad_client = create_bad_client()
        bad_client.tokens.create(lifetime_seconds=None)

def test_token_creation_list():
    with pytest.raises(Exception):
        bad_client = create_bad_client()
        bad_client.tokens.list()

def test_token_creation_delete():
    with pytest.raises(Exception):
        client.tokens.delete(token_id="NotThere")
