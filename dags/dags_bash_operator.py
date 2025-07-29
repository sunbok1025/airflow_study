import pendulum

from airflow.providers.standard.operators.bash import BashOperator
from airflow.sdk import DAG, chain

with DAG(
    dag_id="dags_bash_operator", # airflow 관리도구에서 DAG 제목에 해당하는 부분(파일명도 동일하게 하는 게 좋음)
    schedule="0 0 * * *", # 크론 스케줄 시간 지정 
    start_date=pendulum.datetime(2025, 7, 30, tz="Asia/Seoul"), # 스케줄 시작 날짜
    catchup=False, # 시작날짜가 현재날짜보다 이전일 경우 소급 적용 여부
    tags=["example", "example2", "example3"], # DAG 필터링을 위한 태그 지정
) as dag:
    bash_task1 = BashOperator(
        task_id="bash_task1", # 오퍼레이터 인스턴스(테스크)의 아이디(변수명과 동일하게 하는 게 좋음) 
        bash_command="echo whoami" # 어떤 쉘 스크립트를 수행할건지
    )

    bash_task2 = BashOperator(
        task_id="bash_task2",
        bash_command="echo $HOSTNAME"
    )

    # 테스크의 실행 순서 정의
    bash_task1 >> bash_task2