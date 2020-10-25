import configparser
import psycopg2
from sql_queries import copy_table_queries, insert_table_queries


def load_staging_tables(cur, conn):
    """Execute the queries to copy the data from S3 to the staging tables."""
    for query in copy_table_queries:
        cur.execute(query)
        conn.commit()


def insert_tables(cur, conn):
    """Run the insertion into the main database schema tables from the staging tables."""
    for query in insert_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    """ETL pipeline
    
    1. Get data from S3 and transform it into two staging tables.
    See load_staging_table() 
    
    2. Load the content of the staging table into a set of dimensional tables, designed for
    the data analysis process. 
    See insert_tables() 
    
    Please, inspect the content of the sql_queries.py file
    """
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    cur = conn.cursor()
    
    print("Loading staging tables")
    load_staging_tables(cur, conn)
    print("Inserting data into tables")
    insert_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()