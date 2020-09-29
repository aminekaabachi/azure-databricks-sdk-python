from collections import namedtuple

"""Public token info:  A data structure that describes 
the public metadata of an access token as defined in [1].
[1]: https://docs.microsoft.com/en-gb/azure/databricks/dev-tools/api/latest/tokens#--public-token-info
"""
PublicTokenInfo = namedtuple(
    'PublicTokenInfo', ['token_id', 'creation_time', 'expiry_time', 'comment'])
