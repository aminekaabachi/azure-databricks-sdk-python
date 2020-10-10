from enum import Enum, unique
from typing import List
import attr


@attr.s
class MavenLibrary:
    """MavenLibrary [1].
    [1]: https://docs.microsoft.com/en-gb/azure/databricks/dev-tools/api/latest/libraries#--mavenlibrary
    """
    package: str = attr.ib()
    repo: str = attr.ib(default=None)
    exclusions: List[str] = attr.ib(default=[])


@attr.s
class RCranLibrary:
    """RCranLibrary [1].
    [1]: https://docs.microsoft.com/en-gb/azure/databricks/dev-tools/api/latest/libraries#--rcranlibrary
    """
    package: str = attr.ib()
    repo: str = attr.ib(default=None)


@attr.s
class PythonPyPiLibrary:
    """PythonPyPiLibrary [1].
    [1]: https://docs.microsoft.com/en-gb/azure/databricks/dev-tools/api/latest/libraries#--pythonpypilibrary
    """
    package: str = attr.ib()
    repo: str = attr.ib(default=None)


@attr.s
class Library:
    """Library [1].
    [1]: https://docs.microsoft.com/en-gb/azure/databricks/dev-tools/api/latest/libraries#--library
    """
    jar: str = attr.ib(default=None)
    egg: str = attr.ib(default=None)
    whl: str = attr.ib(default=None)
    pypi: PythonPyPiLibrary = attr.ib(default=None)
    maven: MavenLibrary = attr.ib(default=None)
    cran: RCranLibrary = attr.ib(default=None)


@unique
class LibraryInstallStatus(Enum):
    """LibraryInstallStatus:  The status of a library on a specific cluster [1].
    [1]: https://docs.microsoft.com/en-gb/azure/databricks/dev-tools/api/latest/libraries#--libraryinstallstatus
    """
    PENDING = 'PENDING'
    RESOLVING = 'RESOLVING'
    INSTALLING = 'INSTALLING'
    INSTALLED = 'INSTALLED'
    SKIPPED = 'SKIPPED'
    FAILED = 'FAILED'
    UNINSTALL_ON_RESTART = 'UNINSTALL_ON_RESTART'


@attr.s
class LibraryFullStatus:
    """LibraryFullStatus: The status of the library on a specific cluster [1].
    [1]: https://docs.microsoft.com/en-gb/azure/databricks/dev-tools/api/latest/libraries#--libraryfullstatus
    """
    library: Library = attr.ib()
    status: LibraryInstallStatus = attr.ib()
    messages: List[str] = attr.ib(default=[])
    is_library_for_all_clusters: bool = attr.ib(default=False)


@attr.s
class ClusterLibraryStatuses:
    """ClusterLibraryStatuses [1].
    [1]: https://docs.microsoft.com/en-gb/azure/databricks/dev-tools/api/latest/libraries#--clusterlibrarystatuses
    """
    cluster_id: str = attr.ib()
    library_statuses: List[LibraryFullStatus] = attr.ib()
