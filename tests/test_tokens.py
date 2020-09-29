from .helpers import create_client, create_bad_client
import pytest

client = create_client()

def test_tokens_operations():
    tokens = client.tokens.list()
    new_token = client.tokens.create(lifetime_seconds=None)
    new_tokens = client.tokens.list()
    assert len(tokens) == len(new_tokens)-1
    client.tokens.delete(token_id=new_token.get('token_info').token_id)
    new_tokens = client.tokens.list()
    assert len(tokens) == len(new_tokens)


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
