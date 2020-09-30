from collections import namedtuple
from enum import Enum, unique
from typing import Optional, List, Dict
import attr


@attr.s
class AutoScale:
    """AutoScale:  Range defining the min and max number of cluster workers [1].
    [1]: https://docs.microsoft.com/en-us/azure/databricks/dev-tools/api/latest/clusters#autoscale
    """
    min_workers: int = attr.ib()
    max_workers: int = attr.ib()


@attr.s
class SparkNode:
    """SparkNode: Spark driver or executor configuration [1].
    [1]: https://docs.microsoft.com/en-us/azure/databricks/dev-tools/api/latest/clusters#sparknode
    """
    private_ip: str = attr.ib()
    public_dns: str = attr.ib()
    node_id: str = attr.ib()
    instance_id: str = attr.ib()
    start_timestamp: int = attr.ib()
    host_private_ip: str = attr.ib()


@attr.s
class DbfsStorageInfo:
    """DbfsStorageInfo:  DBFS storage information [1].
    [1]: https://docs.microsoft.com/en-us/azure/databricks/dev-tools/api/latest/clusters#dbfsstorageinfo
    """
    destination: str = attr.ib()


@attr.s
class ClusterLogConf:
    """ClusterLogConf:  Path to cluster log. [1].
    [1]: https://docs.microsoft.com/en-us/azure/databricks/dev-tools/api/latest/clusters#clusterlogconf
    """
    dbfs: DbfsStorageInfo = attr.ib()


@attr.s
class InitScriptInfo:
    """InitScriptInfo:  Path to an init script [1].
    [1]: https://docs.microsoft.com/en-us/azure/databricks/dev-tools/api/latest/clusters#initscriptinfo
    """
    dbfs: DbfsStorageInfo = attr.ib()


@attr.s
class DockerBasicAuth:
    """DockerBasicAuth:  Docker image connection information [1].
    [1]: https://docs.microsoft.com/en-us/azure/databricks/dev-tools/api/latest/clusters#dockerbasicauth
    """
    username: str = attr.ib()
    password: str = attr.ib()


@attr.s
class DockerImage:
    """DockerImage:  Docker image connection information [1].
    [1]: https://docs.microsoft.com/en-us/azure/databricks/dev-tools/api/latest/clusters#dockerimage
    """
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


@attr.s
class LogSyncStatus:
    """LogSyncStatus:  Log delivery status [1].
    [1]: https://docs.microsoft.com/en-us/azure/databricks/dev-tools/api/latest/clusters#logsyncstatus
    """
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


@attr.s
class TerminationParameter:
    """TerminationParameter: Key that provides additional information about why a cluster was terminated [1].
    [1]: https://docs.microsoft.com/en-us/azure/databricks/dev-tools/api/latest/clusters#terminationparameter
    """
    username: str = attr.ib(default=None)
    azure_error_message: str = attr.ib(default=None)
    inactivity_duration_min: int = attr.ib(default=None)
    instance_id: str = attr.ib(default=None)
    azure_error_code: str = attr.ib(default=None)
    instance_pool_id: str = attr.ib(default=None)
    instance_pool_error_code: str = attr.ib(default=None)
    databricks_error_message: str = attr.ib(default=None)


@attr.s
class TerminationReason:
    """TerminationReason: Reason why a cluster was terminated [1].
    [1]: https://docs.microsoft.com/en-us/azure/databricks/dev-tools/api/latest/clusters#TerminationReason
    """
    code: TerminationCode = attr.ib()
    type: TerminationType = attr.ib()
    parameters: TerminationParameter = attr.ib()


@attr.s
class ClusterInfo:
    """ClusterInfo:  Metadata about a cluster [1].
    [1]: https://docs.microsoft.com/en-us/azure/databricks/dev-tools/api/latest/clusters#clusterinfo
    """
    creator_user_name: str = attr.ib()
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
    spark_context_id: int = attr.ib(default=None)
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


@attr.s
class ClusterCloudProviderNodeInfo:
    """ClusterCloudProviderNodeInfo:  Information about an instance supplied by a cloud provider [1].
    [1]: https://docs.microsoft.com/en-us/azure/databricks/dev-tools/api/latest/clusters#clustercloudprovidernodeinfo
    """
    available_core_quota: int = attr.ib(default=None)
    total_core_quota: int = attr.ib(default=None)
    status: List[ClusterCloudProviderNodeStatus] = attr.ib(default=None)


@attr.s
class NodeType:
    """NodeType:  Description of a Spark node type including both the dimensions
    of the node and the instance type on which it will be hosted [1].
    [1]: https://docs.microsoft.com/en-us/azure/databricks/dev-tools/api/latest/clusters#nodetype
    """
    node_type_id: str = attr.ib()
    memory_mb: int = attr.ib()
    num_cores: float = attr.ib()
    description: str = attr.ib()
    instance_type_id: str = attr.ib()
    is_deprecated: bool = attr.ib()
    node_info: ClusterCloudProviderNodeInfo = attr.ib()


@attr.s
class SparkVersion:
    """SparkVersion:  Databricks Runtime version of the cluster.
    [1]: https://docs.microsoft.com/en-us/azure/databricks/dev-tools/api/latest/clusters#sparkversion
    """
    key: str = attr.ib()
    name: str = attr.ib()


@unique
class ListOrder(Enum):
    """ListOrder:  Generic ordering enum for list-based queries [1].
    [1]: https://docs.microsoft.com/en-us/azure/databricks/dev-tools/api/latest/clusters#listorder
    """
    DESC = 'DESC'
    ASC = 'ASC'


@unique
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


@attr.s
class ClusterEventRequest:
    """ClusterEventRequest: Cluster event request structure [1]
    [1]: https://docs.microsoft.com/en-gb/azure/databricks/dev-tools/api/latest/clusters#--request-structure-10
    """
    cluster_id: str = attr.ib()
    start_time: int = attr.ib(default=None)
    end_time: int = attr.ib(default=None)
    order: ListOrder = attr.ib(default=None)
    event_types: List[ClusterEventType] = attr.ib(default=None)
    offset: int = attr.ib(default=None)
    limit: int = attr.ib(default=None)


@unique
class ResizeCause(Enum):
    """ResizeCause:  Reason why a cluster was resized [1].
    [1]: https://docs.microsoft.com/en-us/azure/databricks/dev-tools/api/latest/clusters#resizecause
    """
    AUTOSCALE = 'AUTOSCALE'
    USER_REQUEST = 'USER_REQUEST'
    AUTORECOVERY = 'AUTORECOVERY'


@attr.s
class ClusterSize:
    """ClusterSize:  Cluster size specification [1].
    [1]: https://docs.microsoft.com/en-us/azure/databricks/dev-tools/api/latest/clusters#clustersize
    """
    num_workers: int = attr.ib(default=None)
    autoscale: AutoScale = attr.ib(default=None)


@unique
class ClusterSource(Enum):
    """ClusterSource:  Status code indicating why the cluster was terminated due to a pool failure [1].
    [1]: https://docs.microsoft.com/en-us/azure/databricks/dev-tools/api/latest/clusters#clustersource
    """
    UI = 'UI'
    JOB = 'JOB'
    API = 'API'


@attr.s
class ClusterAttributes:
    """ClusterAttributes:  Common set of attributes set during cluster creation.
    These attributes cannot be changed over the lifetime of a cluster. [1].
    [1]: https://docs.microsoft.com/en-us/azure/databricks/dev-tools/api/latest/clusters#clusterattributes
    """
    spark_version: str = attr.ib()
    node_type_id: str = attr.ib()
    num_workers: int = attr.ib(default=None)
    autoscale: AutoScale = attr.ib(default=None)
    autotermination_minutes: str = attr.ib(default=None)
    driver_node_type_id: str = attr.ib(default=None)
    cluster_id: str = attr.ib(default=None)
    cluster_name: str = attr.ib(default=None)
    cluster_source: ClusterSource = attr.ib(default=None)
    enable_elastic_disk: bool = attr.ib(default=None)
    ssh_public_keys: List[str] = attr.ib(default=None)
    spark_conf: Dict = attr.ib(default=None)
    custom_tags: Dict = attr.ib(default=None)
    cluster_log_conf: ClusterLogConf = attr.ib(default=None)
    init_scripts: List[InitScriptInfo] = attr.ib(default=None)
    docker_image: DockerImage = attr.ib(default=None)
    spark_env_vars: Dict = attr.ib(default=None)
    instance_pool_id: str = attr.ib(default=None)
    policy_id: str = attr.ib(default=None)
    idempotency_token: str = attr.ib(default=None)

@attr.s
class EventDetails:
    """EventDetails:  Cluster event information [1].
    [1]: https://docs.microsoft.com/en-us/azure/databricks/dev-tools/api/latest/clusters#eventdetails
    """
    user: str = attr.ib(default=None)
    reason: TerminationReason = attr.ib(default=None)
    current_num_workers: int = attr.ib(default=None)
    target_num_workers: int = attr.ib(default=None)
    previous_attributes: ClusterAttributes = attr.ib(default=None)
    attributes: ClusterAttributes = attr.ib(default=None)
    previous_cluster_size: ClusterSize = attr.ib(default=None)
    cluster_size: ClusterSize = attr.ib(default=None)
    cause: ResizeCause = attr.ib(default=None)


@attr.s
class ClusterEvent:
    """ClusterEvent:  Cluster event information [1].
    [1]: https://docs.microsoft.com/en-us/azure/databricks/dev-tools/api/latest/clusters#clusterevent
    """
    cluster_id: str = attr.ib()
    timestamp: int = attr.ib(default=None)
    type: ClusterEventType = attr.ib(default=None)
    details: EventDetails = attr.ib(default=None)


@attr.s
class ClusterEventResponse:
    """ClusterEventRequest: Cluster event request response structure [1]
    [1]: https://docs.microsoft.com/en-gb/azure/databricks/dev-tools/api/latest/clusters#--response-structure-5
    """
    events: List[ClusterEvent] = attr.ib(default=None)
    total_count: int = attr.ib(default=None)
    next_page: ClusterEventRequest = attr.ib(default=None)


@attr.s
class ClusterId:
    """ClusterId: represents a cluster id.
    Not official in the API data structures.
    """
    cluster_id: str = attr.ib()


@attr.s
class ClusterResizeRequest:
    """ClusterResizeRequest: represents a resize request.
    Not official in the API data structures.
    """
    cluster_id: str = attr.ib()
    num_workers: int = attr.ib(default=None)
    autoscale: AutoScale = attr.ib(default=None)