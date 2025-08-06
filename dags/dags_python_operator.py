import pendulum
import random

from airflow.providers.standard.operators.python import PythonOperator
from airflow.sdk import DAG, chain

with DAG(
    dag_id="dags_python_operator",
    schedule="30 6 * * *",
    start_date=pendulum.datetime(2025, 7, 30, tz="Asia/Seoul"),
    catchup=False
) as dag:

    def select_fruit():
        fruit = ['APPLE', 'BANANA', 'ORANGE', 'AVOCADO']
        rand_int = random.randint(0, 3)
        print(fruit[rand_int])

    py_task1 = PythonOperator(
        task_id="py_task1",
        python_callable=select_fruit
    )

    py_task1