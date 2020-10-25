import configparser
import psycopg2
from sql_queries import create_table_queries, drop_table_queries


def drop_tables(cur, conn):
    """Drop existing tables
    
    Execute the queries contained in the drop_table_queries list
    See the sql_queries.py
    """
    print("Dropping tables")
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()


def create_tables(cur, conn):
    """Create the man main database schema
    
    Execute the table creation queries contained 
    in the create_table_queries list
    See the sql_queries.py 
    """
    print("Creating database schema")
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()
        #print("executed" + query)


def main():
    """Data modeling creation process"""
    
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    #connection_string = "host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values())
    #print(connection_string)
    
    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    cur = conn.cursor()
    
    print("Cluster connected")
    print(conn)

    drop_tables(cur, conn)
    create_tables(cur, conn)
    
    conn.close()


if __name__ == "__main__":
    main()