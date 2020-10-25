# Data Warehouse using Amazon Redshift

## Introduction

A music streaming startup, Sparkify, has grown their user base and song database and want to move their processes and data onto the cloud. Their data resides in S3, in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.



## Project description

We'll use AWS to build an ETL pipeline for a database hosted on [Amazon Redshift](https://docs.aws.amazon.com/redshift/index.html). The data will be loaded from [Amazon S3](https://docs.aws.amazon.com/s3/?id=docs_gateway) to set of staging tables on the Redshift cluster. From the staging tables set, we'll populate the following analytics tables



![data-modeling](.\data\img\data-modeling.png)

The ETL pipeline uses Python and PostgreSQL.
 **Note:** Although Redshift is based on PostgresSQL, is important to note that Amazon Redshift and PostgreSQL have a number of important [differences](https://docs.aws.amazon.com/redshift/latest/dg/c_redshift-and-postgres-sql.html).

## Project structure
```
P3_Data_Warehouse_Redshift
    │   analytics.py
    │   create_tables.py
    │   etl.py
    │   README.md
    │   sql_queries.py
```
`analytics.py`
Execute some analytics queries to the Redshift created tables. Run `pyhton analytics.py >> analytics_results` in order to get a result file. 

`etl.py`
ETL pipeline. Data is copied from S3 to the staging tables. After that, the data is inserted into the analytics tables. 

`create_tables.py`
Star schema creation.

`sql_queries.py`
Required SQL statements.

## Data

From Amazon S3, the data from two dataset will be copied into two staging tables, created from the dataset schema.

```sql
-- staging events 
CREATE TABLE staging_events(
        artist              VARCHAR,
        auth                VARCHAR,
        firstName           VARCHAR,
        gender              VARCHAR,
        itemInSession       INTEGER,
        lastName            VARCHAR,
        length              FLOAT,
        level               VARCHAR,
        location            VARCHAR,
        method              VARCHAR,
        page                VARCHAR,
        registration        FLOAT,
        sessionId           INTEGER,
        song                VARCHAR,
        status              INTEGER,
        ts                  TIMESTAMP,
        userAgent           VARCHAR,
        userId              INTEGER 
    )
```

```sql
-- staging songs
 CREATE TABLE staging_songs(
        num_songs           INTEGER,
        artist_id           VARCHAR,
        artist_latitude     FLOAT,
        artist_longitude    FLOAT,
        artist_location     VARCHAR,
        artist_name         VARCHAR,
        song_id             VARCHAR,
        title               VARCHAR,
        duration            FLOAT,
        year                INTEGER
    )
```

## Followed steps

1. Schema design

