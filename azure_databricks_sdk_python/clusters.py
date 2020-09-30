from azure_databricks_sdk_python.api import API
from azure_databricks_sdk_python.types.clusters import ClusterInfo, NodeType, SparkVersion

from cattr import structure
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
        if res.status_code == 200:
            return structure(res.json().get('clusters'), List[ClusterInfo])
        else:
            self._handle_error(res)

    def list_node_types(self):
        """Return a list of supported Spark node types. 
        These node types can be used to launch a cluster.

        Returns:
            [NodeType]: The list of available Spark node types.
        """
        endpoint = '/clusters/list-node-types'
        res = self._get(endpoint)
        if res.status_code == 200:
            return structure(res.json().get('node_types'), List[NodeType])
        else:
            self._handle_error(res)
    
    def spark_versions(self):
        """Return the list of available runtime versions. 
        These versions can be used to launch a cluster.


        Returns:
            [SparkVersion]: All the available runtime versions.
        """
        endpoint = '/clusters/spark-versions'
        res = self._get(endpoint)
        if res.status_code == 200:
            return structure(res.json().get('versions'), List[SparkVersion])
        else:
            self._handle_error(res)

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
        if res.status_code == 200:
            return structure(res.json(), ClusterInfo)
        else:
            self._handle_error(res)
