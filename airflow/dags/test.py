from datetime import datetime, timedelta


from airflow.operators.bash import BashOperator
from airflow.operators.docker_operator import DockerOperator


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
    schedule=timedelta(days=1),  # you can use cron here to schedule
    start_date=datetime(2021, 1, 1),
    catchup=False,
    tags=["example"],
    # params={"commit": "000000"},
)

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

task2 = DockerOperator(
    task_id="docker_compose_task",
    image="docker/compose:latest",  # Using the official Docker Compose image
    api_version="auto",
    auto_remove=True,
    command="up",
    docker_url="unix://var/run/docker.sock",  # Connect to the host's Docker socket
    network_mode="bridge",  # Adjust the network mode as needed
    volumes=[
        "/path/to/your/docker-compose-directory:/app"
    ],  # Mount the directory containing your docker-compose.yml
    environment={
        "DOCKER_BUILD": "1",  # Set this environment variable to trigger --build in docker-compose up
    },
    dag=dag,
)


task0 >> task1 >> task2
