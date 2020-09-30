from .helpers import create_client, create_bad_client
import pytest
import cattr
client = create_client()

def test_clusters_operations():
    clusters = client.clusters.list()
    #rint(clusters)
    assert False

def test_cluster_get():
    cluster = client.clusters.get('0918-220215-atria616')
    print(cluster)
    assert False

def test_list_node_types():
    node_types = client.clusters.list_node_types()
    #print(node_types)
    assert False

def test_list_spark_versions():
    spark_versions = client.clusters.spark_versions()
    print(spark_versions)
    assert False

def test_clusters_list_error():
    with pytest.raises(Exception):
        bad_client = create_bad_client()
        bad_client.clusters.list()