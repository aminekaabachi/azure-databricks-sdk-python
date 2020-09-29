from .helpers import create_client

client = create_client()

def test_create_tokens():
    print(client.tokens.create(lifetime_seconds=None))
    assert False

def test_list_tokens():
    print(client.tokens.list())
    assert False

def test_delete_tokens():
    print(client.tokens.delete(token_id="1dd0d7efa02fa2944e16b0cd6a6ecd2d88ebe47bb2d98a7e9ab2ed1df94e2332"))
    assert False