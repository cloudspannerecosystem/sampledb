# SampleDB
[![cloudspannerecosystem](https://circleci.com/gh/cloudspannerecosystem/sampledb.svg?style=svg)](https://circleci.com/gh/cloudspannerecosystem/sampledb)

This application allows you to quickly get a sample database into Cloud Spanner.
It does so by loading data from a CSV file into a Cloud Spanner database.

The data contained in the CSV file is sourced from the "Hacker News - Y
Combinator" BigQuery
[public dataset](https://cloud.google.com/bigquery/public-data/).

Please feel free to report issues and send pull requests, but note that this
application is not officially supported as part of the Cloud Spanner product.

## Setup

### Create an instance

[Create a Cloud Spanner instance](https://cloud.google.com/spanner/docs/quickstart-console)
if you haven't already done so. Remember the instance name, as you'll need it
when running the application.

### Authentication

This sample requires you to have authentication set up. Refer to the
[Authentication Getting Started Guide](https://cloud.google.com/docs/authentication/getting-started)
for instructions on setting up credentials for applications.

### Install Dependencies

* Install [`pip`](https://pip.pypa.io/) and
  [`virtualenv`](https://virtualenv.pypa.io/) if you do not already have them.
  You may want to refer to the [Python Development Environment Setup
  Guide](https://cloud.google.com/python/setup) for Google Cloud Platform for
  instructions.

* Create a virtualenv. Samples are compatible with Python 2.7 and 3.4+.

      virtualenv env
      source env/bin/activate

* Install the dependencies needed to run the samples.

      pip install -r requirements.txt

## Run the application

    python batch_import.py <instance_id> <database_id>

* `<instance_id>`: your Cloud Spanner instance ID.
* `<database_id>`: the Cloud Spanner database ID; the application will create
  and populate this database.
