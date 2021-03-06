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
Use this solution as a full Data Pipeline for taking some public historical data from sfgov (San Francisco Government) repository
related with fire incidents:

https://data.sfgov.org/Public-Safety/Fire-Incidents/wr8u-xric

This Pipeline will download the data source as csv file taking part of extraction procces for data from the specified 
source using basic web scraping tools. Once the csv is downloaded and saved locally in a folder then the program will
load the data into a local Postgres Database, this process could be automated using cloud services
like Lambda Functions (AWS) in a daily basis according toscraping tools. 

Once the csv is downloaded and saved locally then the program will load the data into a local Postgres.

The data copying proccess from the source to one single table that also represents the data dictionary provided.
From this unique table we are able to create some transformations which allows to aggregate the data by some specific
columns like:

* Time period (by year, month and day)
* District (counting the occurrences for each district)
* Battalion (counting the occurrences for each battalion)

Installation
------------

- Python version 3.7.6
- Postgres version 12.2 (Local Installation Preferable)
- DBT-Postgres version 1.0.1 (Virtual environment suggested) via Pypi
- Configure DBT: `profiles.yml` and `dbt_project.yml`. And test DBT config with `dbt_debug`


Requirements
^^^^^^^^^^^^

Install `requirements.txt` with dependencies before running the Pipeline.

To execute the first part of the project (Extract & Load) just run the command: `python run.py` and the Pipeline will
make the following steps:

E-L (Extraction and Load)

- Extract data from source and save this data locally as csv file. The extract module uses `requests` to get a csv directly
from the source.
- Copy the downloaded data to Postgres database considering the data dictionary shared in the same source data page using 
`sqlalchemy`.

After completing this two steps from the Pipeline it may generate a exact copy of the data source in the data warehouse. 
For a daily updating of the data it is important to consider Cloud Services such as AWS Lambda to schedule this job in a
daily basis.

T (Transformation)

- For transformation the tool selected was DBT, to create 3 dimensions by DBT models that represents common aggregations
that some BI teams could use in the future. These three dimensions are: `battallion`, `district`and `time_period`.
Use the command `dbt run --full-refresh` to run DBT and then the new dimensions will be materialized as views in the same
original schema.


Authors
-------

`fire_incidents_extract` was written by `Juan Laverde <juanelveerde@outlook.com>`_.
