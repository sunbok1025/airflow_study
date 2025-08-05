import pendulum

from airflow.providers.standard.operators.python import (
    ExternalPythonOperator,
    PythonOperator,
    PythonVirtualenvOperator,
)
from airflow.sdk import DAG
from airflow.decorators import task

with DAG(
    dag_id="dags_python_task_decorator",
    schedule="0 2 * * 1",
    start_date=pendulum.datetime(2025, 7, 30, tz='Asia/Seoul'),
    catchup=False
) as dag:
        
        @task(task_id='python_task_1')
        def print_context(input):
                print(input)

        python_task_1 = print_context('task_decorator 실행')       