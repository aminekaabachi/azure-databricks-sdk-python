.. _advanced:

Advanced Usage
==============

This document covers some of the SDK more advanced features.


Authenticate using an Azure AD token
------------------------------------

    >>> from azure_databricks_sdk_python import Client, AuthMethods

    >>> client = Client(auth_method=AuthMethods.AZURE_AD_USER, 
                        databricks_instance="<instance>", access_token="<ad_token>")

Authenticate using a service principal
--------------------------------------

    >>> from azure_databricks_sdk_python import Client, AuthMethods

    >>> Client(auth_method=AuthMethods.AZURE_AD_SERVICE_PRINCIPAL,
               databricks_instance="<instance>", access_token="<access_token>", 
               management_token="<management_token>", resource_id="<resource_id>")

.. note::
    You can generate a management token using curl for example:
        ``curl -X GET -H 'Content-Type: application/x-www-form-urlencoded' \
        -d 'grant_type=client_credentials&client_id=<client-id>&resource=https://management.core.windows.net/&client_secret=<client-secret>' \
        https://login.microsoftonline.com//oauth2/token``

.. note::
    You can generate an token using curl for example:
        ``curl -X GET -H 'Content-Type: application/x-www-form-urlencoded' \
        -d 'grant_type=client_credentials&client_id=<client-id>&resource=2ff814a6-3304-4ab8-85cb-cd0e6f879c1d&client_secret=<client-secret>' \
        https://login.microsoftonline.com//oauth2/token``
            
Available operations on clusters
--------------------------------

    >>> client.clusters.list()

.. autofunction:: azure_databricks_sdk_python.clusters.Clusters.list
    :noindex:


---

    >>> client.clusters.list_node_types()

.. autofunction:: azure_databricks_sdk_python.clusters.Clusters.list_node_types
    :noindex:

---

    >>> client.clusters.spark_versions()

.. autofunction:: azure_databricks_sdk_python.clusters.Clusters.spark_versions
    :noindex:

---

    >>> client.clusters.get(...)

.. autofunction:: azure_databricks_sdk_python.clusters.Clusters.get
    :noindex:  

---

    >>> client.clusters.events(...)

.. autofunction:: azure_databricks_sdk_python.clusters.Clusters.events
    :noindex:  

---

    >>> client.clusters.pin(...)

.. autofunction:: azure_databricks_sdk_python.clusters.Clusters.pin
    :noindex:  

---

    >>> client.clusters.unpin(...)

.. autofunction:: azure_databricks_sdk_python.clusters.Clusters.unpin
    :noindex:  

---

    >>> client.clusters.delete(...)

.. autofunction:: azure_databricks_sdk_python.clusters.Clusters.delete
    :noindex:  

---

    >>> client.clusters.permanent_delete(...)

.. autofunction:: azure_databricks_sdk_python.clusters.Clusters.permanent_delete
    :noindex: 

---

    >>> client.clusters.resize(...)

.. autofunction:: azure_databricks_sdk_python.clusters.Clusters.resize
    :noindex: 

---

    >>> client.clusters.restart(...)

.. autofunction:: azure_databricks_sdk_python.clusters.Clusters.restart
    :noindex:   

---

    >>> client.clusters.start(...)

.. autofunction:: azure_databricks_sdk_python.clusters.Clusters.start
    :noindex:   

---

    >>> client.clusters.create(...)

.. autofunction:: azure_databricks_sdk_python.clusters.Clusters.create
    :noindex:  

---

    >>> client.clusters.edit(...)

.. autofunction:: azure_databricks_sdk_python.clusters.Clusters.edit
    :noindex:   

---


Available operations on tokens
------------------------------

.. autofunction:: azure_databricks_sdk_python.tokens.Tokens.list
    :noindex:   

---

.. autofunction:: azure_databricks_sdk_python.tokens.Tokens.create
    :noindex:   

---

.. autofunction:: azure_databricks_sdk_python.tokens.Tokens.delete
    :noindex:   

---

Available operations on secrets
-------------------------------

.. autofunction:: azure_databricks_sdk_python.secrets.Secrets.list
    :noindex:   

---

.. autofunction:: azure_databricks_sdk_python.secrets.Secrets.put
    :noindex:   

---

.. autofunction:: azure_databricks_sdk_python.secrets.Secrets.delete
    :noindex:   

---

.. autofunction:: azure_databricks_sdk_python.secrets.ACLS.list
    :noindex:   

---

.. autofunction:: azure_databricks_sdk_python.secrets.ACLS.get
    :noindex:   

---

.. autofunction:: azure_databricks_sdk_python.secrets.ACLS.put
    :noindex:   

---

.. autofunction:: azure_databricks_sdk_python.secrets.ACLS.delete
    :noindex:   

---

.. autofunction:: azure_databricks_sdk_python.secrets.Scopes.list
    :noindex:   

---

.. autofunction:: azure_databricks_sdk_python.secrets.Scopes.create
    :noindex:   

---

.. autofunction:: azure_databricks_sdk_python.secrets.Scopes.delete
    :noindex:   

---