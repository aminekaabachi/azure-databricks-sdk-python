.. _install:

Installation of the SDK
=======================

This part of the documentation covers the installation of azure-databricks-sdk-python.
The first step to using any software package is getting it properly installed.


$ python -m pip install  azure-databricks-sdk-python
----------------------------------------------------

To install azure-databricks-sdk-python, simply run this simple command in your terminal of choice::

    $ python -m pip install  azure-databricks-sdk-python

Get the Source Code
-------------------

azure-databricks-sdk-python is actively developed on GitHub, where the code is
`always available <https://github.com/aminekaabachi/ azure-databricks-sdk-python>`_.

You can either clone the public repository::

    $ git clone git://github.com/aminekaabachi/azure-databricks-sdk-python.git

Or, download the `tarball <https://github.com/aminekaabachi/azure-databricks-sdk-python/tarball/master>`_::

    $ curl -OL https://github.com/aminekaabachi/azure-databricks-sdk-python/tarball/master
    # optionally, zipball is also available (for Windows users).

Once you have a copy of the source, you can embed it in your own Python
package, or install it into your site-packages easily::

    $ cd azure-databricks-sdk-python
    $ python -m pip install .