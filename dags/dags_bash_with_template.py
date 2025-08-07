import pendulum

from airflow.providers.standard.operators.bash import BashOperator
from airflow.sdk import DAG, chain

with DAG(
    dag_id="dags_bash_with_template",
    schedule="10 0 * * *",
    start_date=pendulum.datetime(2025, 7, 30, tz="Asia/Seoul"),
    catchup=False
) as dag:

    bash_task1 = BashOperator(
        task_id='bash_task1',
        bash_command='echo "data_interval_end: {{ data_interval_end }}"'
    )

    bash_task2 = BashOperator(
        task_id='bash_task2',
        env={
            'START_DATE':'{{ data_interval_start | ds }}', # YYYY-MM-DD 형식으로 출력
            'END_DATE':'{{ data_interval_end | ds }}'
        },
        bash_command='eho $START_DATE && $END_DATE'
    )

    bash_task3 = BashOperator(
        task_id='bash_task3',
        bash_command='ehco run_id: {{ run_id }}'
    )

    bash_task1 >> bash_task2 >> bash_task3    