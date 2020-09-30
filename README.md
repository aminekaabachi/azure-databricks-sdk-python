# Azure Databricks SDK for Python

[![Workflow Status](https://img.shields.io/github/workflow/status/aminekaabachi/azure-databricks-sdk-python/Unit%20Tests/master?style=flat-square)](https://github.com/aminekaabachi/azure-databricks-sdk-python/actions?query=workflow%3A%22Unit+Tests%22)
[![Coveralls github](https://img.shields.io/coveralls/github/aminekaabachi/azure-databricks-sdk-python?style=flat-square)](https://coveralls.io/github/aminekaabachi/azure-databricks-sdk-python?branch=master)
[![PyPI](https://img.shields.io/pypi/v/azure-databricks-sdk-python?style=flat-square)](https://pypi.org/project/azure-databricks-sdk-python/)
[![GitHub](https://img.shields.io/github/license/aminekaabachi/azure-databricks-sdk-python?style=flat-square)](https://github.com/aminekaabachi/azure-databricks-sdk-python/blob/master/LICENSE)


A Python SDK for the [Azure Databricks REST API 2.0](https://docs.azuredatabricks.net/api/latest/index.html)

### Install
You can install the package using pip:
```bash
pip install azure-databricks-sdk-python
```

## Usage

```python

from azure-databricks-sdk-python import Client

client = Client(databricks_instance="<instance>", personal_access_token="<token>")

```

## Implementation Progress

Please refer to the progress below:

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


