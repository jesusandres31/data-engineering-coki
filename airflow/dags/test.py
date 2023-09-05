from datetime import datetime, timedelta

from airflow.operators.bash import BashOperator
from airflow.operators.docker_operator import DockerOperator
from docker.types import Mount

from airflow import DAG

dag_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "email": ["airflow@test.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1),
    # 'wait_for_downstream': False,
    # 'sla': timedelta(hours=2),
    # 'execution_timeout': timedelta(seconds=300),
    # 'on_failure_callback': some_function, # or list of functions
    # 'on_success_callback': some_other_function, # or list of functions
    # 'on_retry_callback': another_function, # or list of functions
    # 'sla_miss_callback': yet_another_function, # or list of functions
    # 'trigger_rule': 'all_success'
}

dag = DAG(
    "test1",
    description="My ETL DAG",
    default_args=dag_args,
    schedule=timedelta(days=1),
    start_date=datetime(2021, 1, 1),
    catchup=False,
)

# inside container ETL path = /opt/airflow/ETL
extract_compose_file = "/opt/airflow/ETL/extract/docker-compose.yml"
transform_compose_file = "/opt/airflow/ETL/transform/docker-compose.yml"
load_compose_file = "/opt/airflow/ETL/load/docker-compose.yml"

# tasks
task0 = BashOperator(
    task_id="bash_func0",
    bash_command="pwd",
    dag=dag,
)

task1 = BashOperator(
    task_id="bash_func1",
    bash_command="ls /opt/airflow/ETL",
    dag=dag,
)

extract_task = DockerOperator(
    task_id="ejecutar_extract",
    image="docker",
    api_version="auto",
    auto_remove=True,
    command="up --build",
    docker_url="unix://var/run/docker.sock",
    network_mode="bridge",
    mounts=[
        Mount(source=extract_compose_file, target="/docker-compose.yam", type="bind"),
    ],
    dag=dag,
)

# run
task0 >> task1 >> extract_task
