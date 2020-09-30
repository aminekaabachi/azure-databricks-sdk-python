# Azure Databricks SDK Python

[![Workflow Status](https://img.shields.io/github/workflow/status/aminekaabachi/azure-databricks-sdk-python/Unit%20Tests/master?style=flat-square)](https://github.com/aminekaabachi/azure-databricks-sdk-python/actions?query=workflow%3A%22Unit+Tests%22)
[![Coveralls github](https://img.shields.io/coveralls/github/aminekaabachi/azure-databricks-sdk-python?style=flat-square)](https://coveralls.io/github/aminekaabachi/azure-databricks-sdk-python?branch=master)
[![PyPI](https://img.shields.io/pypi/v/azure-databricks-sdk-python?style=flat-square)](https://pypi.org/project/azure-databricks-sdk-python/)
[![Downloads](https://img.shields.io/pypi/dm/azure-databricks-sdk-python?style=flat-square)](https://pypi.org/project/azure-databricks-sdk-python/)
[![GitHub](https://img.shields.io/github/license/aminekaabachi/azure-databricks-sdk-python?style=flat-square)](https://github.com/aminekaabachi/azure-databricks-sdk-python/blob/master/LICENSE)


**azure-databricks-sdk-python** is a Python SDK for the [`Azure Databricks REST API 2.0`](<https://docs.microsoft.com/en-gb/azure/databricks/dev-tools/api/latest/>).

-----------------

Easily, perform all the operations as if on the databricks UI:
```python
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
```

## Beloved Features

**azure-databricks-sdk-python** is ready for your use-case:

- Supports Personal Access token authentification.
- Supports Azure AD authentification.
- Supports the use of Service Principals.
- Custom types for the API results and requests.
- Force mode to bypass the types validation (in case you want to go hardcore).

Requests officially supports 3.6+, and runs great on PyPy.

## Implementation Progress

Please refer to the progress below:

| Feature  | Progress |
| :--- | :---: | 
| Auth | 80% |
| Error handling | 30% |

| API  | Progress |
| :--- | :---: | 
| Clusters API | 80% |
| Clusters Policies API | 0% |
| DBFS API  | 0% |
| Groups API  | 0% |
| Instance Pools API | 0% |
| Jobs API | 0% |
| Libraries API | 0% |
| MLflow API | 0% |
| Permissions API | 0% |
| SCIM API | 0% |
| Secrets API | 0% |
| Token API | 100% ✔ |
| Token Management API | 0% |
| Workspace API | 0% |

## Documentation

Check the documentation on [readthedocs.org](https://azure-databricks-sdk-python.readthedocs.io/en/latest/).
---
