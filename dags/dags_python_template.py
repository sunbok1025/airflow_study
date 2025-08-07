import pendulum

from airflow.sdk import DAG
from airflow.decorators import task
from airflow.operators.python import PythonOperator

with DAG(
    dag_id='dags_python_template',
    schedule='30 9 * * *',
    start_date=pendulum.datetime(2025, 8, 5, tz='Asia/Seoul'),
    catchup=False
) as dag:
    
    # 1. PythonOperator의 op_kwargs 파라미터를 통해 진자 템플릿에 변수를 주는 방식
    def python_function(start_date, end_date, **kwargs):
        print(start_date)
        print(end_date)
    
    python_task1 = PythonOperator(
        task_id='python_task1',
        python_callable=python_function,
        op_kwargs={'start_date':'{{data_interval_start | ds}}', 'end_date':'{{data_interval_end | ds}}'}
    )

    # 2. kwargs에 있는 템플릿 변수들을 꺼내쓰는 방식
    @task(task_id='python_task2')
    def python_function2(**kwargs):
        print(kwargs)
        print('ds: ' + kwargs['ds'])
        print('ts: ' + kwargs['ts'])
        print('data_interval_start: ' + str(kwargs['data_interval_start']))
        print('data_interval_end: ' + str(kwargs['data_interval_end']))
        print('task_instance: ' + str(kwargs['ti']))

    python_task1 >> python_function2()