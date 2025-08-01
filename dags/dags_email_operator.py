import pendulum

from airflow.providers.smtp.operators.smtp import EmailOperator
from airflow.sdk import DAG, chain

with DAG(
    dag_id="dags_email_operator",
    schedule="0 8 1 * *",
    start_date=pendulum.datetime(2025, 7, 30, tz="Asia/Seoul"),
    catchup=False
) as dag:
    send_email_task = EmailOperator(
        task_id='send_email_task',
        conn_id='conn_smtp_gmail', #Airflow connection에서 설정한 ID 값 지정
        to='sunbok1025@naver.com',
        subject='Airflow 성공 메일',
        html_content='Airflow 작업이 완료되었습니다.'
    )