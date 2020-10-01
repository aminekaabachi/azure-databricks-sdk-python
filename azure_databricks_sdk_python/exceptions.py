from requests import HTTPError


class APIError(Exception):
    """  """


class ResourceAlreadyExists(ValueError):
    """  """


class AuthorizationError(HTTPError):
    """  """


class ResourceDoesNotExist(ValueError):
    """  """


class IoError(HTTPError):
    """  """


class InvalidParameterValue(HTTPError):
    """  """


class LibraryNotFound(ValueError):
    """  """


class InvalidState(HTTPError):
    """  """


class LibraryInstallFailed(ValueError):
    """  """


class UnknownFormat(AttributeError):
    """  """


class MaxNotebookSizeExceeded(HTTPError):
    """  """


class MaxBlockSizeExceeded(HTTPError):
    """  """


class MaxReadSizeExceeded(HTTPError):
    """  """


class DirectoryNotEmpty(HTTPError):
    """  """


ERROR_CODES = {
    "RESOURCE_DOES_NOT_EXIST": ResourceDoesNotExist,
    "RESOURCE_ALREADY_EXISTS": ResourceAlreadyExists,
    "IO_ERROR": IoError,
    "INVALID_PARAMETER_VALUE": InvalidParameterValue,
    "INVALID_STATE": InvalidState,
    "MAX_NOTEBOOK_SIZE_EXCEEDED": MaxNotebookSizeExceeded,
    "MAX_BLOCK_SIZE_EXCEEDED": MaxBlockSizeExceeded,
    "MAX_READ_SIZE_EXCEEDED": MaxReadSizeExceeded,
    "DIRECTORY_NOT_EMPTY": DirectoryNotEmpty,
}
