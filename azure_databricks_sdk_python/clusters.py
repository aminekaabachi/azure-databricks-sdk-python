from azure_databricks_sdk_python.api import API
from azure_databricks_sdk_python.types.clusters import *

from cattr import structure, unstructure
from typing import List


class Clusters(API):
    """The Clusters API allows you to create, start, edit, list, terminate, and delete clusters.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def list(self):
        """Return information about all pinned clusters, active clusters, 
        up to 70 of the most recently terminated all-purpose clusters in the past 30 days, 
        and up to 30 of the most recently terminated job clusters in the past 30 days. 

        Returns:
            [ClusterInfo]: A list of clusters.
        """
        endpoint = '/clusters/list'
        res = self._get(endpoint)
        return self._safe_handle(res, res.json().get('clusters'), List[ClusterInfo])

    def list_node_types(self):
        """Return a list of supported Spark node types. 
        These node types can be used to launch a cluster.

        Returns:
            [NodeType]: The list of available Spark node types.
        """
        endpoint = '/clusters/list-node-types'
        res = self._get(endpoint)
        return self._safe_handle(res, res.json().get('node_types'), List[NodeType])

    def spark_versions(self):
        """Return the list of available runtime versions. 
        These versions can be used to launch a cluster.


        Returns:
            [SparkVersion]: All the available runtime versions.
        """
        endpoint = '/clusters/spark-versions'
        res = self._get(endpoint)
        return self._safe_handle(res, res.json().get('versions'), List[SparkVersion])

    def get(self, cluster_id):
        """Retrieve the information for a cluster given its identifier. 
        Clusters can be described while they are running or up to 30 days after they are terminated.

        Args:
            cluster_id (str):The cluster about which to retrieve information. This field is required.

        Returns:
            ClusterInfo: Metadata about a cluster.
        """
        endpoint = '/clusters/get'
        data = {'cluster_id': cluster_id}
        res = self._get(endpoint, data)
        return self._safe_handle(res, res.json(), ClusterInfo)

    def events(self, req: ClusterEventRequest, force: bool = True):
        """Retrieve a list of events about the activity of a cluster. 

        Args:
            req (ClusterEventRequest): Cluster event request structure. This field is required.
            force (bool): If false, it will check that req is a dict 
            then pass it as is, with no type validation.
        Returns:
            ClusterEventResponse: Cluster event request response structure.
        """
        endpoint = '/clusters/events'
        data = self._validate(req, ClusterEventRequest, force)
        res = self._post(endpoint, unstructure(data))
        return self._safe_handle(res, res.json(), ClusterEventResponse)

    def pin(self, cluster_id):
        """Ensure that an all-purpose cluster configuration is retained 
        even after a cluster has been terminated for more than 30 days. 
        Pinning ensures that the cluster is always returned by the List API. 
        Pinning a cluster that is already pinned has no effect.

        Args:
            cluster_id (str):The cluster to pin. This field is required.

        Returns:
            ClusterId: in case of success or will raise an exception.
        """
        endpoint = '/clusters/pin'
        data = {'cluster_id': cluster_id}
        res = self._post(endpoint, data)
        return self._safe_handle(res, data, ClusterId)

    def unpin(self, cluster_id):
        """Allows the cluster to eventually be removed from the list returned 
        by the List API. Unpinning a cluster that is not pinned has no effect.


        Args:
            cluster_id (str):The cluster to pin. This field is required.

        Returns:
            ClusterId: in case of success or will raise an exception.
        """
        endpoint = '/clusters/unpin'
        data = {'cluster_id': cluster_id}
        res = self._post(endpoint, data)
        return self._safe_handle(res, data, ClusterId)

    def delete(self, cluster_id):
        """Terminate a cluster given its ID. 

        Args:
            cluster_id (str): The cluster to be terminated. 
            This field is required.

        Returns:
            ClusterId: in case of success or will raise an exception.
        """
        endpoint = '/clusters/delete'
        data = {'cluster_id': cluster_id}
        res = self._post(endpoint, data)
        return self._safe_handle(res, data, ClusterId)

    def permanent_delete(self, cluster_id):
        """Permanently delete a cluster. 

        Args:
            cluster_id (str): The cluster to be permanently deleted. 
            This field is required.

        Returns:
            ClusterId: in case of success or will raise an exception.
        """
        endpoint = '/clusters/permanent-delete'
        data = {'cluster_id': cluster_id}
        res = self._post(endpoint, data)
        return self._safe_handle(res, data, ClusterId)

    def resize(self, req: ClusterResizeRequest, force: bool = True):
        """Resize a cluster to have a desired number of workers. 
        The cluster must be in the RUNNING state.

        Args:
            req (ClusterResizeRequest): Cluster resize request structure. This field is required.
            force (bool): If false, it will check that req is a dict 
            then pass it as is, with no type validation.
        Returns:
            ClusterId: in case of success or will raise an exception.
        """
        endpoint = '/clusters/resize'
        data = self._validate(req, ClusterResizeRequest, force)
        res = self._post(endpoint, unstructure(data))
        return self._safe_handle(res, ClusterId(cluster_id=data.get('cluster_id')))

    def restart(self, cluster_id):
        """Restart a cluster given its ID.
         The cluster must be in the RUNNING state.

        Args:
            cluster_id (str): The cluster to be started.
            This field is required.

        Returns:
            ClusterId: in case of success or will raise an exception.
        """
        endpoint = '/clusters/restart'
        data = {'cluster_id': cluster_id}
        res = self._post(endpoint, data)
        return self._safe_handle(res, data, ClusterId)

    def start(self, cluster_id):
        """Start a terminated cluster given its ID.

        Args:
            cluster_id (str): The cluster to be started.
            This field is required.

        Returns:
            ClusterId: in case of success or will raise an exception.
        """
        endpoint = '/clusters/start'
        data = {'cluster_id': cluster_id}
        res = self._post(endpoint, data)
        return self._safe_handle(res, data, ClusterId)

    def create(self, req: ClusterAttributes, force: bool = True):
        """Create a new Apache Spark cluster. 
        This method acquires new instances from the cloud provider if necessary. 

        Args:
            req (ClusterAttributes): Common set of attributes set during cluster creation. This field is required.
            force (bool): If false, it will check that req is a dict 
            then pass it as is, with no type validation.
        Returns:
            ClusterId: in case of success or will raise an exception.
        """
        endpoint = '/clusters/create'
        data = self._validate(req, ClusterAttributes, force)
        res = self._post(endpoint, unstructure(data))
        return self._safe_handle(res, res.json(), ClusterId)

    def edit(self, req: ClusterAttributes, force: bool = True):
        """Edit the configuration of a cluster 
        to match the provided attributes and size.

        Args
            req (ClusterAttributes): Common set of attributes set during cluster creation. This field is required.
            force (bool): If false, it will check that req is a dict 
            then pass it as is, with no type validation.
        Returns:
            ClusterId: in case of success or will raise an exception.
        """
        endpoint = '/clusters/edit'
        data = self._validate(req, ClusterAttributes, force)
        res = self._post(endpoint, unstructure(data))
        return self._safe_handle(res, res.json(), ClusterId)
