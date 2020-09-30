from typing import Optional
import attr

@attr.s
class PublicTokenInfo:
    """Public token info:  A data structure that describes
    the public metadata of an access token as defined in [1].
    [1]: https://docs.microsoft.com/en-gb/azure/databricks/dev-tools/api/latest/tokens#--public-token-info
    """
    token_id: str = attr.ib()
    creation_time: int = attr.ib()
    expiry_time: int = attr.ib()
    comment: str = attr.ib()



@attr.s
class TokenId:
    """TokenId: represents a token id.
    Not official in the API data structures.
    """
    token_id: str = attr.ib()