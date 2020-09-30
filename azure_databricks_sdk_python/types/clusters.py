from collections import namedtuple
from enum import Enum, unique
from typing import Optional, List, Dict
import attr

# AutoScale:  Range defining the min and max number of cluster workers [1].
# [1]: https://docs.microsoft.com/en-us/azure/databricks/dev-tools/api/latest/clusters#autoscale


@attr.s
class AutoScale:
    min_workers: int = attr.ib()
    max_workers: int = attr.ib()

# SparkNode: Spark driver or executor configuration [1].
# [1]: https://docs.microsoft.com/en-us/azure/databricks/dev-tools/api/latest/clusters#sparknode


@attr.s
class SparkNode:
    private_ip: str = attr.ib()
    public_dns: str = attr.ib()
    node_id: str = attr.ib()
    instance_id: str = attr.ib()
    start_timestamp: int = attr.ib()
    host_private_ip: str = attr.ib()


# DbfsStorageInfo:  DBFS storage information [1].
# [1]: https://docs.microsoft.com/en-us/azure/databricks/dev-tools/api/latest/clusters#dbfsstorageinfo
@attr.s
class DbfsStorageInfo:
    destination: str = attr.ib()

# ClusterLogConf:  Path to cluster log. [1].
# [1]: https://docs.microsoft.com/en-us/azure/databricks/dev-tools/api/latest/clusters#clusterlogconf


@attr.s
class ClusterLogConf:
    dbfs: DbfsStorageInfo = attr.ib()


# InitScriptInfo:  Path to an init script [1].
# [1]: https://docs.microsoft.com/en-us/azure/databricks/dev-tools/api/latest/clusters#initscriptinfo
@attr.s
class InitScriptInfo:
    dbfs: DbfsStorageInfo = attr.ib()


# DockerBasicAuth:  Docker image connection information [1].
# [1]: https://docs.microsoft.com/en-us/azure/databricks/dev-tools/api/latest/clusters#dockerbasicauth
@attr.s
class DockerBasicAuth:
    username: str = attr.ib()
    password: str = attr.ib()

# DockerImage:  Docker image connection information [1].
# [1]: https://docs.microsoft.com/en-us/azure/databricks/dev-tools/api/latest/clusters#dockerimage


@attr.s
class DockerImage:
    url: str = attr.ib()
    basic_auth: DockerBasicAuth = attr.ib()


@unique
class ClusterState(Enum):
    """ClusterState:  State of a cluster[1].
    [1]: https://docs.microsoft.com/en-us/azure/databricks/dev-tools/api/latest/clusters#clusterstate
    """
    PENDING = 'PENDING'
    RUNNING = 'RUNNING'
    RESTARTING = 'RESTARTING'
    RESIZING = 'RESIZING'
    TERMINATING = 'TERMINATING'
    TERMINATED = 'TERMINATED'
    ERROR = 'ERROR'
    UNKNOWN = 'UNKNOWN'

# LogSyncStatus:  Log delivery status [1].
# [1]: https://docs.microsoft.com/en-us/azure/databricks/dev-tools/api/latest/clusters#logsyncstatus


@attr.s
class LogSyncStatus:
    last_attempted: int = attr.ib()
    last_exception: str = attr.ib()


@unique
class PoolClusterTerminationCode(Enum):
    """PoolClusterTerminationCode:  Status code indicating why the cluster was terminated due to a pool failure [1].
    [1]: https://docs.microsoft.com/en-us/azure/databricks/dev-tools/api/latest/clusters#poolclusterterminationcode
    """
    INSTANCE_POOL_MAX_CAPACITY_FAILURE = 'INSTANCE_POOL_MAX_CAPACITY_FAILURE'
    INSTANCE_POOL_NOT_FOUND_FAILURE = 'INSTANCE_POOL_NOT_FOUND_FAILURE'


@unique
class TerminationType(Enum):
    """TerminationType: Reason why the cluster was terminated [1].
    [1]: https://docs.microsoft.com/en-us/azure/databricks/dev-tools/api/latest/clusters#terminationtype
    """
    SUCCESS = 'SUCCESS'
    CLIENT_ERROR = 'CLIENT_ERROR'
    SERVICE_FAULT = 'SERVICE_FAULT'
    CLOUD_FAILURE = 'CLOUD_FAILURE'


@unique
class TerminationCode(Enum):
    """TerminationCode:  Status code indicating why the cluster was terminated [1].
    [1]: https://docs.microsoft.com/en-us/azure/databricks/dev-tools/api/latest/clusters#terminationcode
    """
    USER_REQUEST = 'USER_REQUEST'
    JOB_FINISHED = 'JOB_FINISHED'
    INACTIVITY = 'INACTIVITY'
    CLOUD_PROVIDER_SHUTDOWN = 'CLOUD_PROVIDER_SHUTDOWN'
    COMMUNICATION_LOST = 'COMMUNICATION_LOST'
    CLOUD_PROVIDER_LAUNCH_FAILURE = 'CLOUD_PROVIDER_LAUNCH_FAILURE'
    SPARK_STARTUP_FAILURE = 'SPARK_STARTUP_FAILURE'
    INVALID_ARGUMENT = 'INVALID_ARGUMENT'
    UNEXPECTED_LAUNCH_FAILURE = 'UNEXPECTED_LAUNCH_FAILURE'
    INTERNAL_ERROR = 'INTERNAL_ERROR'
    SPARK_ERROR = 'SPARK_ERROR'
    METASTORE_COMPONENT_UNHEALTHY = 'METASTORE_COMPONENT_UNHEALTHY'
    DBFS_COMPONENT_UNHEALTHY = 'DBFS_COMPONENT_UNHEALTHY'
    AZURE_RESOURCE_PROVIDER_THROTTLING = 'AZURE_RESOURCE_PROVIDER_THROTTLING'
    AZURE_RESOURCE_MANAGER_THROTTLING = 'AZURE_RESOURCE_MANAGER_THROTTLING'
    NETWORK_CONFIGURATION_FAILURE = 'NETWORK_CONFIGURATION_FAILURE'
    DRIVER_UNREACHABLE = 'DRIVER_UNREACHABLE'
    DRIVER_UNRESPONSIVE = 'DRIVER_UNRESPONSIVE'
    INSTANCE_UNREACHABLE = 'INSTANCE_UNREACHABLE'
    CONTAINER_LAUNCH_FAILURE = 'CONTAINER_LAUNCH_FAILURE'
    INSTANCE_POOL_CLUSTER_FAILURE = 'INSTANCE_POOL_CLUSTER_FAILURE'
    REQUEST_REJECTED = 'REQUEST_REJECTED'
    INIT_SCRIPT_FAILURE = 'INIT_SCRIPT_FAILURE'
    TRIAL_EXPIRED = 'TRIAL_EXPIRED'


# TerminationParameter: Key that provides additional information about why a cluster was terminated [1].
# [1]: https://docs.microsoft.com/en-us/azure/databricks/dev-tools/api/latest/clusters#terminationparameter
@attr.s
class TerminationParameter:
    username: str = attr.ib()
    azure_error_message: str = attr.ib(default=None)
    inactivity_duration_min: int = attr.ib(default=None)
    instance_id: str = attr.ib(default=None)
    azure_error_code: str = attr.ib(default=None)
    instance_pool_id: str = attr.ib(default=None)
    instance_pool_error_code: str = attr.ib(default=None)
    databricks_error_message: str = attr.ib(default=None)

# TerminationReason: Reason why a cluster was terminated [1].
# [1]: https://docs.microsoft.com/en-us/azure/databricks/dev-tools/api/latest/clusters#TerminationReason


@attr.s
class TerminationReason:
    code: TerminationCode = attr.ib()
    type: TerminationType = attr.ib()
    parameters: TerminationParameter = attr.ib()


# ClusterInfo:  Metadata about a cluster [1].
# [1]: https://docs.microsoft.com/en-us/azure/databricks/dev-tools/api/latest/clusters#clusterinfo
@attr.s
class ClusterInfo:
    cluster_id: str = attr.ib()
    creator_user_name: str = attr.ib()
    spark_context_id: int = attr.ib()
    cluster_name: str = attr.ib()
    spark_version: str = attr.ib()
    node_type_id: str = attr.ib()
    driver_node_type_id: str = attr.ib()
    autotermination_minutes: int = attr.ib()
    enable_elastic_disk: bool = attr.ib()
    state: ClusterState = attr.ib()
    state_message: str = attr.ib()
    start_time: int = attr.ib()
    last_state_loss_time: int = attr.ib()
    default_tags: Dict = attr.ib()
    jdbc_port: int = attr.ib(default=None)
    cluster_memory_mb: int = attr.ib(default=None)
    cluster_cores: float = attr.ib(default=None)
    cluster_log_status: LogSyncStatus = attr.ib(default=None)
    termination_reason: TerminationReason = attr.ib(default=None)
    terminated_time: int = attr.ib(default=None)
    last_activity_time: int = attr.ib(default=None)
    instance_pool_id: str = attr.ib(default=None)
    spark_env_vars: Dict = attr.ib(default=None)
    docker_image: DockerImage = attr.ib(default=None)
    init_scripts: List[InitScriptInfo] = attr.ib(default=None)
    cluster_log_conf: ClusterLogConf = attr.ib(default=None)
    spark_conf: Dict = attr.ib(default=None)
    driver: SparkNode = attr.ib(default=None)
    executors: List[SparkNode] = attr.ib(default=None)
    num_workers: int = attr.ib(default=None)
    autoscale: AutoScale = attr.ib(default=None)

@unique
class ClusterCloudProviderNodeStatus(Enum):
    """ClusterCloudProviderNodeStatus:  Status of an instance supplied by a cloud provider [1].
    [1]: https://docs.microsoft.com/en-us/azure/databricks/dev-tools/api/latest/clusters#clustercloudprovidernodestatus
    """
    NotEnabledOnSubscription = 'NotEnabledOnSubscription'
    NotAvailableInRegion = 'NotAvailableInRegion'

# ClusterCloudProviderNodeInfo:  Information about an instance supplied by a cloud provider [1].
# [1]: https://docs.microsoft.com/en-us/azure/databricks/dev-tools/api/latest/clusters#clustercloudprovidernodeinfo
@attr.s
class ClusterCloudProviderNodeInfo:
    available_core_quota: int = attr.ib(default=None)
    total_core_quota: int = attr.ib(default=None)
    status: List[ClusterCloudProviderNodeStatus] = attr.ib(default=None)

# NodeType:  Description of a Spark node type including both the dimensions
# of the node and the instance type on which it will be hosted [1].
# [1]: https://docs.microsoft.com/en-us/azure/databricks/dev-tools/api/latest/clusters#nodetype
@attr.s
class NodeType:
    node_type_id: str = attr.ib()
    memory_mb: int = attr.ib()
    num_cores: float = attr.ib()
    description: str = attr.ib()
    instance_type_id: str = attr.ib()
    is_deprecated: bool = attr.ib()
    node_info: ClusterCloudProviderNodeInfo = attr.ib()


# SparkVersion:  Databricks Runtime version of the cluster.
# [1]: https://docs.microsoft.com/en-us/azure/databricks/dev-tools/api/latest/clusters#sparkversion
@attr.s
class SparkVersion:
    key: str = attr.ib()
    name: str = attr.ib()

# ClusterEvent:  Cluster event information [1].
#  [1]: https://docs.microsoft.com/en-us/azure/databricks/dev-tools/api/latest/clusters#clusterevent
ClusterEvent = namedtuple(
    'ClusterEvent', ['cluster_id', 'timestamp', 'type', 'details'])


class ClusterEventType(Enum):
    """ClusterEventType:  Type of a cluster event [1].
    [1]: https://docs.microsoft.com/en-us/azure/databricks/dev-tools/api/latest/clusters#clustereventtype
    """
    CREATING = 'CREATING'
    DID_NOT_EXPAND_DISK = 'DID_NOT_EXPAND_DISK'
    EXPANDED_DISK = 'EXPANDED_DISK'
    FAILED_TO_EXPAND_DISK = 'FAILED_TO_EXPAND_DISK'
    INIT_SCRIPTS_STARTING = 'INIT_SCRIPTS_STARTING'
    INIT_SCRIPTS_FINISHED = 'INIT_SCRIPTS_FINISHED'
    STARTING = 'STARTING'
    RESTARTING = 'RESTARTING'
    TERMINATING = 'TERMINATING'
    EDITED = 'EDITED'
    RUNNING = 'RUNNING'
    RESIZING = 'RESIZING'
    UPSIZE_COMPLETED = 'UPSIZE_COMPLETED'
    NODES_LOST = 'NODES_LOST'
    DRIVER_HEALTHY = 'DRIVER_HEALTHY'
    DRIVER_UNAVAILABLE = 'DRIVER_UNAVAILABLE'
    SPARK_EXCEPTION = 'SPARK_EXCEPTION'
    DRIVER_NOT_RESPONDING = 'DRIVER_NOT_RESPONDING'
    DBFS_DOWN = 'DBFS_DOWN'
    METASTORE_DOWN = 'METASTORE_DOWN'
    NODE_BLACKLISTED = 'NODE_BLACKLISTED'
    PINNED = 'PINNED'
    UNPINNED = 'UNPINNED'



# EventDetails:  Cluster event information [1].
# [1]: https://docs.microsoft.com/en-us/azure/databricks/dev-tools/api/latest/clusters#eventdetails
EventDetails = namedtuple(
    'EventDetails', ['current_num_workers', 'target_num_workers', 'previous_attributes', 'attributes',
                     'previous_cluster_size', 'cluster_size', 'cause', 'reason', 'user'])


# ClusterAttributes:  Common set of attributes set during cluster creation.
# These attributes cannot be changed over the lifetime of a cluster. [1].
# [1]: https://docs.microsoft.com/en-us/azure/databricks/dev-tools/api/latest/clusters#clusterattributes
ClusterAttributes = namedtuple(
    'ClusterAttributes', ['cluster_name', 'spark_version', 'spark_conf', 'node_type_id',
                          'driver_node_type_id', 'ssh_public_keys', 'custom_tags', 'cluster_log_conf', 'init_scripts',
                          'docker_image', 'spark_env_vars', 'autotermination_minutes', 'enable_elastic_disk',
                          'instance_pool_id', 'cluster_source', 'policy_id'])


# ClusterSize:  Cluster size specification [1].
# [1]: https://docs.microsoft.com/en-us/azure/databricks/dev-tools/api/latest/clusters#clustersize
ClusterSize = namedtuple(
    'ClusterSize', ['num_workers', 'autoscale'])


class ListOrder(Enum):
    """ListOrder:  Generic ordering enum for list-based queries [1].
    [1]: https://docs.microsoft.com/en-us/azure/databricks/dev-tools/api/latest/clusters#listorder
    """
    DESC = 'DESC'
    ASC = 'ASC'


class ResizeCause(Enum):
    """ResizeCause:  Reason why a cluster was resized [1].
    [1]: https://docs.microsoft.com/en-us/azure/databricks/dev-tools/api/latest/clusters#resizecause
    """
    AUTOSCALE = 'AUTOSCALE'
    USER_REQUEST = 'USER_REQUEST'
    AUTORECOVERY = 'AUTORECOVERY'


class ClusterSource(Enum):
    """ClusterSource:  Status code indicating why the cluster was terminated due to a pool failure [1].
    [1]: https://docs.microsoft.com/en-us/azure/databricks/dev-tools/api/latest/clusters#clustersource
    """
    UI = 'UI'
    JOB = 'JOB'
    API = 'API'
