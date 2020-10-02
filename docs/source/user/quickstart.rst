.. _quickstart:

Quickstart
==========


Eager to get started? This page gives a good introduction in how to get started
with our SDK.

First, make sure that:

* SDK is :ref:`installed <install>`

Let's get started with some simple examples.


Authenticate
------------

The easiest way to access the Databricks APIs is through using a `personal access token <https://docs.databricks.com/dev-tools/api/latest/authentication.html#generate-a-personal-access-token>`_.

Begin by importing the :class:`azure_databricks_sdk_python.clients.Client` class from SDK module::

    >>> from azure_databricks_sdk_python import Client

You can now instantiate a client object. You need to pass the databricks instance (format: adb-<XXX>.<X>.azuredatabricks.net) and your token:

    >>> client = Client(databricks_instance=<instance>, personal_access_token=<token>)

If you try to evaluate ``client`` now:

    >>> client
    <azure_databricks_sdk_python.client.PersonalAccessTokenClient object at 0x10a03a700>

You now have a PersonalAccessTokenClient that allows you to access Databricks APIs with a personal access token.

.. Note::
    No internal connection test is done when you instantiate a client! 

You can use client.test_connection() to do a connection test, as the following:

    >>> client.test_connection()
    True

Generate a token
----------------

You can create a new token by using the following:

    >>> token = client.tokens.create(comment="A happy token from the docs.")

All the return token is an instance of :class:`azure_databricks_sdk_python.types.tokens.Token`.
If you evaluate it, you get:

    >>> token
    Token(token_value='<redacted>', token_info=PublicTokenInfo(token_id='<redacted>', creation_time=1601551181943, expiry_time=1609327181943, comment='A happy token from the docs.'))

The attributes of the tokens are accessible through dot chaining:

    >>> token.token_info.comment
    'A happy token from the docs.'

Create a cluster
----------------

You can create a new cluster using the following:

    >>> cluster = client.tokens.create(attributes)

``attributes`` are instance of :class:`azure_databricks_sdk_python.types.clusters.ClusterAttributes`.

So before creating a cluster you need to create define its attributes. Here is an example:


    >>> attributes = ClusterAttributes(cluster_name="my-cute-cluster", 
                                       spark_version="7.2.x-scala2.12",
                                       node_type_id="Standard_F4s", 
                                       autoscale=autoscale)
    

.. Note::
    You need at least the ``cluster_name``, ``node_type_id``, ``spark_version`` and (``autoscale`` or ``num_workers``) to be able to create a valid cluster.

Now ``create`` will return an instance of :class:`azure_databricks_sdk_python.types.clusters.ClusterInfo`. You can access it's properties through dot chainin, for example:

    >>> cluster.cluster_id
    '0918-220215-atria616'


Get cluster details
-------------------

You can access an existing cluster details using the following synthax.

    >>> details = client.clusters.get(cluster_id='<cluster_id>')

It will return an instance of :class:`azure_databricks_sdk_python.types.clusters.ClusterInfo`. You can access it's properties through dot chainin, for example:

    >>> details.state.name
    'TERMINATED'

Terminate a cluster
-------------------

You can easily terminate a cluster using this function:

    >>> terminated = client.clusters.delete(cluster_id='<cluster_id>')

It will return an instance of :class:`azure_databricks_sdk_python.types.clusters.ClusterId`. You can then get it by using:

    >>> terminated.cluster_id
    '0918-220215-atria616'
