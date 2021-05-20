# Getting some context variables and macros
# References: 
# - https://airflow.apache.org/docs/apache-airflow/stable/macros-ref.html
# - https://godatadriven.com/blog/the-zen-of-python-and-apache-airflow/
# Note: The code below was taken (and modified) from the Udactiy learning materials

import datetime
import logging

from airflow import DAG
from airflow.models import Variable
from airflow.operators.python_operator import PythonOperator
from airflow.hooks.S3_hook import S3Hook


def log_details(*args, **kwargs):
    #
    # Extracts ds, run_id, prev_ds,execution_date,next_ds from the kwargs (context), and log them
    # NOTE: Look here for context variables passed in on context:
    #       https://airflow.apache.org/docs/apache-airflow/stable/macros-ref.html
    # 
    #
    ds = kwargs['ds'] # kwargs[]
    run_id = kwargs['run_id'] # kwargs[]
    previous_ds = kwargs.get('previous_ds') # kwargs.get('')
    next_ds = kwargs.get('next_ds') # kwargs.get('')
    execution_date = kwargs['execution_date']

    logging.info(f"Execution date is {ds}")
    logging.info(f"Execution (logical) date is {execution_date}")
    logging.info(f"My run id is {run_id}")
    if previous_ds:
        logging.info(f"My previous run was on {previous_ds}")
    if next_ds:
        logging.info(f"My next run will be {next_ds}")

dag = DAG(
    'context_and_templating,
    schedule_interval="@daily",
    start_date=datetime.datetime.now() - datetime.timedelta(days=2) # force 2 days before
)

# The PythonOperator with provide_context=True passes the Airflow context to the given callable :) 
list_task = PythonOperator(
    task_id="log_details",
    python_callable=log_details,
    provide_context=True,
    dag=dag
)