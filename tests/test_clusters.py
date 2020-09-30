from .helpers import create_client, create_bad_client
from azure_databricks_sdk_python.types.clusters import *

import pytest
import cattr

client = create_client()
attributes = {
    'cluster_name': 'test-cluster-from-dict-forced',
    'spark_version': '7.2.x-scala2.12',
    'node_type_id': 'Standard_D3_v2',
    'spark_conf': {
        'spark.speculation': True
    },
    'num_workers': 1
}

def test_clusters_create_dict_forced():

    created_id = client.clusters.create(attributes, True)
    deleted_id = client.clusters.delete(cluster_id=created_id.cluster_id)
    assert created_id.cluster_id == deleted_id.cluster_id


def test_clusters_create_terminate_and_delete_obj():
    # create cluser
    spark_conf = {'spark.speculation': True}
    autoscale = AutoScale(min_workers=0, max_workers=1)
    attributes = ClusterAttributes(cluster_name="test-cluster-from-obj",
                                   spark_version="7.2.x-scala2.12",
                                   node_type_id="Standard_D3_v2",
                                   spark_conf=spark_conf,
                                   autoscale=autoscale)
    created_id = client.clusters.create(attributes)

    # terminate it
    terminated_id = client.clusters.delete(cluster_id=created_id.cluster_id)

    # delete it
    delete_id = client.clusters.permanent_delete(cluster_id=created_id.cluster_id)

    assert created_id.cluster_id == terminated_id.cluster_id
    assert created_id.cluster_id == delete_id.cluster_id


def test_cluster_unpin_pin():
    created_id = client.clusters.create(attributes, False)
    unpinned = client.clusters.unpin(cluster_id=created_id.cluster_id)
    pinned = client.clusters.pin(cluster_id=created_id.cluster_id)
    unpinned = client.clusters.unpin(cluster_id=created_id.cluster_id)
    client.clusters.permanent_delete(cluster_id=created_id.cluster_id)
    assert unpinned.cluster_id == pinned.cluster_id
