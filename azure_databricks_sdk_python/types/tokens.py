from typing import Optional
import attr

# Public token info:  A data structure that describes
# the public metadata of an access token as defined in [1].
# [1]: https://docs.microsoft.com/en-gb/azure/databricks/dev-tools/api/latest/tokens#--public-token-info


@attr.s
class PublicTokenInfo:
    token_id: str = attr.ib()
    creation_time: int = attr.ib()
    expiry_time: int = attr.ib()
    comment: str = attr.ib()
