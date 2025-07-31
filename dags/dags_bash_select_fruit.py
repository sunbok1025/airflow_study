import pendulum

from airflow.providers.standard.operators.bash import BashOperator
from airflow.sdk import DAG, chain

with DAG(
    dag_id="dags_bash_select_fruit",
    schedule="10 0 * * 6#1",
    start_date=pendulum.datetime(2025, 7, 30, tz="Asia/Seoul"),
    catchup=False
) as dag:

    task1_orange = BashOperator(
        task_id="task1_orange",
        bash_commands="/opt/airflow/plugins/shell/select_fruit.sh ORANGE"
    )

    task1_avocado = BashOperator(
        task_id="task1_avocado",
        bash_commands="/opt/airflow/plugins/shell/select_fruit.sh AVOCADO"
    )

    task1_orange >> task1_avocado