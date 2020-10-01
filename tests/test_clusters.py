from .helpers import create_client, create_bad_client
from azure_databricks_sdk_python.types.clusters import *

import pytest
import cattr
import time


client = create_client()

def create_cluster_and_wait(name):
    autoscale = AutoScale(min_workers=0, max_workers=1)
    attributes = ClusterAttributes(cluster_name="test-cluster-"+name,
                                   spark_version="7.2.x-scala2.12",
                                   node_type_id="Standard_F4s",
                                   autoscale=autoscale)
    created = client.clusters.create(attributes)

    while True:
        time.sleep(30)
        get_id = client.clusters.get(cluster_id=created.cluster_id)
        state = get_id.state
        if state in [ClusterState.RUNNING, ClusterState.TERMINATED, ClusterState.ERROR]:
            break

    return created.cluster_id


attributes = {
    'cluster_name': 'test-cluster-from-dict-forced',
    'spark_version': '7.2.x-scala2.12',
    'node_type_id': 'Standard_F4s',
    'spark_conf': {
        'spark.speculation': True
    },
    'num_workers': 1
}


def test_clusters_list():
    list = client.clusters.list()
    assert isinstance(list, List)


def test_clusters_list_node_types():
    list = client.clusters.list_node_types()
    assert len(list) > 0
    assert isinstance(list[0], NodeType)


def test_clusters_list_spark_versions():
    list = client.clusters.spark_versions()
    assert len(list) > 0
    assert isinstance(list[0], SparkVersion)


def test_clusters_resize_restart():
    cluster_id = create_cluster_and_wait("resize-restart")
    autoscale = AutoScale(min_workers=0, max_workers=2)
    resized = client.clusters.resize(ClusterResizeRequest(
        cluster_id=cluster_id, autoscale=autoscale))
    assert cluster_id == resized.cluster_id

    client.clusters.restart(cluster_id=cluster_id)

    while True:
            time.sleep(30)
            get_id = client.clusters.get(cluster_id=cluster_id)
            state = get_id.state
            if state in [ClusterState.RUNNING, ClusterState.TERMINATED, ClusterState.ERROR]:
                break

    get_id = client.clusters.get(cluster_id=cluster_id)
    state = get_id.state
    assert state == ClusterState.RUNNING

    client.clusters.permanent_delete(cluster_id=cluster_id)

def test_clusters_edit_start():
    cluster_id = create_cluster_and_wait("edit-start")
    client.clusters.delete(cluster_id=cluster_id)

    while True:
            time.sleep(30)
            get_id = client.clusters.get(cluster_id=cluster_id)
            state = get_id.state
            if state in [ClusterState.TERMINATED, ClusterState.ERROR]:
                break

    get_id = client.clusters.get(cluster_id=cluster_id)
    state = get_id.state
    assert state == ClusterState.TERMINATED

    autoscale = AutoScale(min_workers=0, max_workers=1)
    attributes = ClusterAttributes(cluster_id=cluster_id,
                                   cluster_name="test-cluster-edited",
                                   spark_version="7.2.x-scala2.12",
                                   node_type_id="Standard_F4s",
                                   autoscale=autoscale
                                   )

    client.clusters.edit(attributes)
    get_id = client.clusters.get(cluster_id=cluster_id)
    assert get_id.cluster_name == "test-cluster-edited"

    # client.clusters.start(cluster_id=cluster_id)

    # while True:
    #     time.sleep(30)
    #     get_id = client.clusters.get(cluster_id=cluster_id)
    #     state = get_id.state
    #     if state in [ClusterState.RUNNING, ClusterState.ERROR]:
    #         break

    # get_id = client.clusters.get(cluster_id=cluster_id)
    # state = get_id.state
    # assert state == ClusterState.RUNNING

    client.clusters.permanent_delete(cluster_id=cluster_id)

def test_clusters_create_dict_forced():
    created_id = client.clusters.create(attributes, True)
    get_id = client.clusters.get(cluster_id=created_id.cluster_id)
    deleted_id = client.clusters.permanent_delete(cluster_id=created_id.cluster_id)
    assert created_id.cluster_id == deleted_id.cluster_id
    assert created_id.cluster_id == get_id.cluster_id


def test_clusters_events():
    created_id = client.clusters.create(attributes, True)
    events = client.clusters.events(ClusterEventRequest(created_id.cluster_id))
    assert len(events.events) == 1
    deleted_id = client.clusters.permanent_delete(cluster_id=created_id.cluster_id)
    # events = client.clusters.events(ClusterEventRequest(created_id.cluster_id))
    # assert len(events.events) == 2


def test_clusters_create_terminate_and_delete_obj():
    # create cluser
    spark_conf = {'spark.speculation': True}
    autoscale = AutoScale(min_workers=0, max_workers=1)
    attributes = ClusterAttributes(cluster_name="test-cluster-from-obj",
                                   spark_version="7.2.x-scala2.12",
                                   node_type_id="Standard_F4s",
                                   spark_conf=spark_conf,
                                   autoscale=autoscale)
    created_id = client.clusters.create(attributes)

    # terminate it
    terminated_id = client.clusters.delete(cluster_id=created_id.cluster_id)

    # delete it
    delete_id = client.clusters.permanent_delete(
        cluster_id=created_id.cluster_id)

    assert created_id.cluster_id == terminated_id.cluster_id
    assert created_id.cluster_id == delete_id.cluster_id


def test_cluster_unpin_pin():
    created_id = client.clusters.create(attributes, False)
    unpinned = client.clusters.unpin(cluster_id=created_id.cluster_id)
    pinned = client.clusters.pin(cluster_id=created_id.cluster_id)
    unpinned = client.clusters.unpin(cluster_id=created_id.cluster_id)
    client.clusters.permanent_delete(cluster_id=created_id.cluster_id)
    assert unpinned.cluster_id == pinned.cluster_id
