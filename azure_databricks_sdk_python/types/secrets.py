from enum import Enum, unique
import attr


@unique
class AclPermission(Enum):
    """AclPermission:  The ACL permission levels for secret ACLs applied to secret scopes [1].
    [1]: https://docs.microsoft.com/en-us/azure/databricks/dev-tools/api/latest/secrets#--aclpermission
    """
    READ = 'READ'
    WRITE = 'WRITE'
    MANAGE = 'MANAGE'


@attr.s
class AclItem:
    """AclItem: An item representing an ACL rule applied to the given principal (user or group) on the associated scope point [1].
    [1]: https://docs.microsoft.com/en-us/azure/databricks/dev-tools/api/latest/secrets#--aclitem
    """
    principal: str = attr.ib()
    permission: AclPermission = attr.ib()



@attr.s
class SecretMetadata:
    """SecretMetadata: The metadata about a secret. Returned when listing secrets. Does not contain the actual secret value [1].
    [1]: https://docs.microsoft.com/en-us/azure/databricks/dev-tools/api/latest/secrets#--secretmetadata
    """
    key: str = attr.ib()
    last_updated_timestamp: int = attr.ib()


@unique
class ScopeBackendType(Enum):
    """ScopeBackendType:  The type of secret scope backend [1].
    [1]: https://docs.microsoft.com/en-us/azure/databricks/dev-tools/api/latest/secrets#--scopebackendtype
    """
    AZURE_KEYVAULT = 'AZURE_KEYVAULT'
    DATABRICKS = 'DATABRICKS'


@attr.s
class SecretScope:
    """SecretScope: An organizational resource for storing secrets. Secret scopes can be different types, and ACLs can be applied to control permissions for all secrets within a scope [1].
    [1]: https://docs.microsoft.com/en-us/azure/databricks/dev-tools/api/latest/secrets#--secretscope
    """
    name: str = attr.ib()
    backend_type: ScopeBackendType = attr.ib()

