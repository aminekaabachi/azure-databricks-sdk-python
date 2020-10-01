from azure_databricks_sdk_python.api import API
from azure_databricks_sdk_python.types.tokens import PublicTokenInfo, TokenId, Token
from azure_databricks_sdk_python.types.secrets import *
from cattr import structure, unstructure
from typing import List


class Secrets(API):
    """The Secrets API allows you to manage secrets, secret scopes, and access permissions. 
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.acls = ACLS(**kwargs)
        self.scopes = Scopes(**kwargs)

    def list(self, scope: str):
        """List the secret keys that are stored at this scope. 
        This is a metadata-only operation; you cannot retrieve secret data using this API.
        You must have READ permission to make this call.

        Args:
            scope (str): The name of the scope whose secrets you want to list. This field is required.

        Returns:
            List[SecretMetadata]: Metadata information of all secrets contained within the given scope.
        """
        endpoint = '/secrets/list'
        data = {'scope': scope}
        res = self._get(endpoint, data)
        return self._safe_handle(res, res.json().get('secrets', []), List[SecretMetadata])

    def put(self, scope: str, key: str, string_value: str = None, bytes_value: bytes = None):
        """Create or modify a secret from a Databricks-backed scope.

        Args:
            scope (str): The name of the scope to which the secret will be associated with. This field is required.
            key (str): A unique name to identify the secret. This field is required.
            string_value (str, optional): this value will be stored in UTF-8 (MB4) form. Defaults to None.
            bytes_value (bytes, optional): this value will be stored as bytes. Defaults to None.

        Returns:
            bool: True
        """
        endpoint = '/secrets/put'

        data = {'scope': scope,
                'key': key}

        if (string_value):
            data = {'string_value': string_value, **data}
        elif (bytes_value):
            data = {'bytes_value': bytes_value, **data}

        res = self._post(endpoint, data)
        return self._safe_handle(res, True)

    def delete(self, scope: str, key: str):
        """Deletes a secret from a Databricks-backed scope.

        Args:
            scope (str): The name of the scope that contains the secret to delete. This field is required.
            key (str): Name of the secret to delete. This field is required.

        Returns:
            bool: True
        """
        endpoint = '/secrets/delete'

        data = {'scope': scope,
                'key': key}

        res = self._post(endpoint, data)
        return self._safe_handle(res, True)


class ACLS(API):
    """The ACLs API allows you to manage access permissions. 
    Works only for premium workspaces.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def list(self, scope: str):
        """List the ACLs set on the given scope.

        Args:
            scope (str): The name of the scope to fetch ACL information from. This field is required.

        Returns:
            List[AclItem]: The associated ACLs rule applied to principals in the given scope.
        """
        endpoint = '/secrets/acls/list'
        data = {'scope': scope}
        res = self._get(endpoint, data)
        return self._safe_handle(res, res.json().get('items', []), List[AclItem])

    def get(self, scope: str, principal: str):
        """Describe the details about the given ACL, such as the group and permission.

        Args:
            scope (str): The name of the scope to fetch ACL information from. This field is required.
            principal (str): The principal to fetch ACL information for. This field is required.

        Returns:
            AclItem: An item representing an ACL rule.
        """
        endpoint = '/secrets/acls/get'
        data = {'scope': scope, 'principal': principal}
        res = self._get(endpoint, data)
        return self._safe_handle(res, res.json(), AclItem)

    def put(self, scope: str, principal: str, permission: AclPermission):
        """Create or overwrite the ACL associated 
        with the given principal (user or group) on the specified scope point.

        Args:
            scope (str): The name of the scope to apply permissions to. This field is required.
            principal (str): The principal to which the permission is applied. This field is required.
            permission (AclPermission): The permission level applied to the principal. This field is required.

        Returns:
            bool: True
        """
        endpoint = '/secrets/acls/put'
        data = {'scope': scope, 'principal': principal,
                'permission': unstructure(permission)}
        res = self._post(endpoint, data)
        return self._safe_handle(res, True)

    def delete(self, scope: str, principal: str):
        """Delete the given ACL on the given scope.

        Args:
            scope (str): The name of the scope to remove permissions from. This field is required.
            principal (str): The principal to remove an existing ACL from. This field is required.

        Returns:
            bool: True
        """
        endpoint = '/secrets/acls/delete'
        data = {'scope': scope, 'principal': principal}
        res = self._post(endpoint, data)
        return self._safe_handle(res, True)


class Scopes(API):
    """The ACLs API allows you to manage secret scopes/
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def list(self):
        """List all secret scopes available in the workspace.

        Returns:
            [SecretScope]: The available secret scopes.
        """
        endpoint = '/secrets/scopes/list'

        res = self._get(endpoint)
        return self._safe_handle(res, res.json().get('scopes', []), List[SecretScope])

    def create(self, scope: str, initial_manage_principal: str = None):
        """Create a Databricks-backed secret scope in which secrets are stored 
        in Databricks-managed storage and encrypted with a cloud-based specific encryption key.

        Args:
            scope (str): Scope name requested by the user. Scope names are unique. This field is required.
            initial_manage_principal (str, optional): The principal that is initially 
            granted MANAGE permission to the created scope. Defaults to None.

        Returns:
            bool: True
        """
        endpoint = '/secrets/scopes/create'

        data = {'scope': scope}

        if initial_manage_principal:
            data = {'initial_manage_principal': initial_manage_principal, **data}

        res = self._post(endpoint, data)
        return self._safe_handle(res, True)

    def delete(self, scope: str):
        """Delete a secret scope.

        Args:
            scope (str): Name of the scope to delete. This field is required.

        Returns:
            bool: True
        """
        endpoint = '/secrets/scopes/delete'

        data = {'scope': scope}

        res = self._post(endpoint, data)
        return self._safe_handle(res, True)
