fire_incidents_extract
======================

.. image:: https://img.shields.io/pypi/v/fire_incidents_extract.svg
    :target: https://pypi.python.org/pypi/fire_incidents_extract
    :alt: Latest PyPI version

.. image:: https://travis-ci.org/kragniz/cookiecutter-pypackage-minimal.png
   :target: https://travis-ci.org/kragniz/cookiecutter-pypackage-minimal
   :alt: Latest Travis CI build status

An opinionated, minimal cookiecutter template for Python packages

Usage
-----
Use this solution as a full Data Pipeline from taking public data from sfgov (San Francisco Government) repository:

https://data.sfgov.org/Public-Safety/Fire-Incidents/wr8u-xric

Specifically it will download the source data as csv file as part of extraction data from the source using basic web
scraping tools. Once the csv is downloaded and saved locally then the program will load the data into a local Postgres
Database, this process could be automated using cloud services like Lambda Functions (AWS) in a daily basis according to
updating times for this dataset.

We are copying the data from the source to one single table that represents the data dictionary provided.
From this unique table we are able to create some transformations which allows to aggregate the data by some specific
columns like:

* Time period (by year, month and day)
* District (counting the occurrences for each district)
* battalion (counting the occurrences for each battalion)

Installation
------------



Requirements
^^^^^^^^^^^^

Compatibility
-------------

Licence
-------

Authors
-------

`fire_incidents_extract` was written by `Juan Laverde <juanelveerde@outlook.com>`_.
