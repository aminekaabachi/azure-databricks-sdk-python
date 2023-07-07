.. azure-databricks-sdk-python documentation master file, created by
   sphinx-quickstart on Tue Sep 29 21:14:25 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Azure Databricks SDK Python
===========================

.. warning::
    This project has been archived and is no longer actively maintained or supported. 
    We highly recommend migrating to the official Databricks SDK for Python available at https://github.com/databricks/databricks-sdk-py.

Release v\ |version|. (:ref:`Installation <install>`)

.. image:: https://img.shields.io/github/workflow/status/aminekaabachi/azure-databricks-sdk-python/Unit%20Tests/master?style=flat-square
    :target: https://github.com/aminekaabachi/azure-databricks-sdk-python/actions?query=workflow%3A%22Unit+Tests%22
    
.. image:: https://img.shields.io/coveralls/github/aminekaabachi/azure-databricks-sdk-python?style=flat-square
    :target: https://coveralls.io/github/aminekaabachi/azure-databricks-sdk-python?branch=master

.. image:: https://img.shields.io/pypi/v/azure-databricks-sdk-python?style=flat-square
    :target: https://pypi.org/project/azure-databricks-sdk-python/

.. image:: https://img.shields.io/pypi/dm/azure-databricks-sdk-python?style=flat-square
    :target: https://pypi.org/project/azure-databricks-sdk-python/

.. image:: https://img.shields.io/github/license/aminekaabachi/azure-databricks-sdk-python?style=flat-square)
    :target: https://github.com/aminekaabachi/azure-databricks-sdk-python/blob/master/LICENSE

**azure-databricks-sdk-python** is a Python SDK for the `Azure Databricks REST API 2.0 <https://docs.microsoft.com/en-gb/azure/databricks/dev-tools/api/latest/>`_.

---

Easily, perform all the operations as if on the Databricks UI::


      from azure_databricks_sdk_python import Client
      from azure_databricks_sdk_python.types.clusters import AutoScale, ClusterAttributes

      client = Client(databricks_instance="<instance>", personal_access_token="<token>")
      spark_conf = {'spark.speculation': True}
      autoscale = AutoScale(min_workers=0, max_workers=1)
      attributes = ClusterAttributes(cluster_name="my-cluster",
                                    spark_version="7.2.x-scala2.12",
                                    node_type_id="Standard_D3_v2",
                                    spark_conf=spark_conf,
                                    autoscale=autoscale)
      created = client.clusters.create(attributes)
      print(created.cluster_id)


Beloved Features
----------------

**azure-databricks-sdk-python** is ready for your use-case:

- Clear standard to access to APIs.
- Contains custom types for the API results and requests.
- Support for Personal Access token authentification.
- Support for Azure AD authentification.
- Support for the use of Azure AD service principals.
- Allows free-style API calls with a force mode -(bypass types validation).
- Error handeling and proxy support.

Officially supports 3.6+, and runs great on PyPy.

The User Guide
--------------

This part of the documentation, which is mostly prose, begins with some
background information about azure-databricks-sdk-python, then focuses on step-by-step
instructions for getting the most out of it.

.. toctree::
   :maxdepth: 2

   user/install
   user/quickstart
   user/advanced

The API Documentation
---------------------

If you are looking for information on a specific function, class, or method,
this part of the documentation is for you.

.. toctree::
   :maxdepth: 2

   api

Miscellaneous
-------------

.. toctree::
   :maxdepth: 1

   updates

There are no more guides. 
You are now guideless.
Good luck.