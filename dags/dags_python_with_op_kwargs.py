import pendulum
import random

from airflow.providers.standard.operators.python import PythonOperator
from airflow.sdk import DAG, chain
from common.common_func import regist2

with DAG(
    dag_id='dags_python_with_op_kwargs',
    schedule='30 6 * * *',
    start_date=pendulum.datetime(2025, 8, 1, tz='Asia/Seoul'),
    catchup=False
) as dag:

    regist2_task1 = PythonOperator(
        task_id='regist2_task1',
        python_callable=regist2,
        op_args=['sbkim', 'man', 'kr', 'seoul'],
        op_kwargs={'email':'sungok1025@gmail.com', 'phone':'010'}
    )

    regist2_task1