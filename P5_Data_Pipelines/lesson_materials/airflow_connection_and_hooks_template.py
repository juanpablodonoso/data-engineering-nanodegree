# This is a sample template to test the connection 
# to an AWS S3 bucket and listing all the contained keys
# Note: This was taken from the Udacity learning materials



import datetime
import logging

from airflow import DAG
from airflow.models import Variable
from airflow.operators.python_operator import PythonOperator
from airflow.hooks.S3_hook import S3Hook


def list_keys():
    """List the keys for a connected bucket"""
    hook = S3Hook(aws_conn_id='aws_credentials')
    bucket = Variable.get('')
    prefix = Variable.get('')
    logging.info(f"Listing Keys from {bucket}/{prefix}")
    keys = hook.list_keys(bucket, prefix=prefix)
    for key in keys:
        logging.info(f"- s3://{bucket}/{key}")


dag = DAG(
        's3_hook_test',
        start_date=datetime.datetime.now()) # 1 day schedule 

list_task = PythonOperator(
    task_id="list_keys",
    python_callable=list_keys,
    dag=dag
)