from .helpers import create_client

client = create_client()

def test_tokens():
    tokens = client.tokens.list()
    new_token = client.tokens.create(lifetime_seconds=None)
    new_tokens = client.tokens.list()
    assert len(tokens)==len(new_tokens)-1
    client.tokens.delete(token_id=new_token.get('token_info').token_id)
    new_tokens = client.tokens.list()
    assert len(tokens)==len(new_tokens)
