import configparser
import psycopg2
from sql_queries import counting_queries_dict


def run_count_queries(cur,conn):
    """
    Run the counting queries contained in the 
    counting_queries_dict (see the sql_queries.py).
    
    The results are printed using a table format.
    """
    print("{:<15} {:<15}".format("Query", "Count"))
    for k,v in counting_queries_dict.items():
        cur.execute(v)
        results = cur.fetchone()
        print ("{:<15} {:<15}".format(k,results[0]))
        
        
        

def main():
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    cur = conn.cursor()

    run_count_queries(cur,conn)
    conn.close()


if __name__ == "__main__":
    main()