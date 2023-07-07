# Azure Databricks SDK Python

> **Warning**
> This project has been archived and is no longer actively maintained or supported. We highly recommend migrating to the official Databricks SDK for Python available at https://github.com/databricks/databricks-sdk-py.

[![Workflow Status](https://img.shields.io/github/workflow/status/aminekaabachi/azure-databricks-sdk-python/Unit%20Tests/master?style=flat-square)](https://github.com/aminekaabachi/azure-databricks-sdk-python/actions?query=workflow%3A%22Unit+Tests%22)
[![Coveralls github](https://img.shields.io/coveralls/github/aminekaabachi/azure-databricks-sdk-python?style=flat-square)](https://coveralls.io/github/aminekaabachi/azure-databricks-sdk-python?branch=master)
[![PyPI](https://img.shields.io/pypi/v/azure-databricks-sdk-python?style=flat-square)](https://pypi.org/project/azure-databricks-sdk-python/)
[![Downloads](https://img.shields.io/pypi/dm/azure-databricks-sdk-python?style=flat-square)](https://pypi.org/project/azure-databricks-sdk-python/)
[![Docs](https://readthedocs.org/projects/azure-databricks-sdk-python/badge/?version=latest&style=flat-square)](https://azure-databricks-sdk-python.readthedocs.io/en/latest/)
[![GitHub](https://img.shields.io/github/license/aminekaabachi/azure-databricks-sdk-python?style=flat-square)](https://github.com/aminekaabachi/azure-databricks-sdk-python/blob/master/LICENSE)

**azure-databricks-sdk-python** is a Python SDK for the [`Azure Databricks REST API 2.0`](https://docs.microsoft.com/en-gb/azure/databricks/dev-tools/api/latest/).

---

Easily, perform all the operations as if on the Databricks UI:

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

- Clear standard to access to APIs.
- Contains custom types for the API results and requests.
- Support for Personal Access token authentification.
- Support for Azure AD authentification.
- Support for the use of Azure AD service principals.
- Allows free-style API calls with a force mode -(bypass types validation).
- Error handeling and proxy support.

Officially supports 3.6+, and runs great on PyPy.

## Implementation Progress

Please refer to the progress below:

| Feature          | Progress |
| :--------------- | :------: |
| Authentification |  100% ✔  |
| Custom types     |   25%    |
| API Wrappers     |   25%    |
| Error handling   |   80%    |
| Proxy support    |    0%    |
| Documentation    |   20%    |

As for specific API wrappers:

| API                   | Progress |
| :-------------------- | :------: |
| Clusters API          |  100% ✔  |
| Secrets API           |  100% ✔  |
| Token API             |  100% ✔  |
| Jobs API              |    0%    |
| DBFS API              |    0%    |
| Groups API            |    0%    |
| Libraries API         |    0%    |
| Workspace API         |    0%    |
| Clusters Policies API |    0%    |
| Instance Pools API    |    0%    |
| MLflow API            |    0%    |
| Permissions API       |    0%    |
| SCIM API              |    0%    |
| Token Management API  |    0%    |

## Documentation

Check the documentation on [readthedocs.org](https://azure-databricks-sdk-python.readthedocs.io/en/latest/).

---
