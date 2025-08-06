import pendulum
import random

from airflow.providers.standard.operators.python import PythonOperator
from airflow.sdk import DAG, chain
from common.common_func import regist

with DAG(
    dag_id='dags_python_with_op_args',
    schedule='30 6 * * *',
    start_date=pendulum.datetime(2025, 8, 1, tz='Asia/Seoul'),
    catchup=False
) as dag:

    regist_task1 = PythonOperator(
        task_id='regist_task1',
        python_callable=regist,
        op_args=['sbkim', 'man', 'kr', 'seoul']
    )

    regist_task1