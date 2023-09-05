from datetime import datetime, timedelta

from airflow.providers.docker.operators.docker import DockerOperator

from airflow import DAG

dag_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "email": ["airflow@test.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

dag = DAG(
    "etl",
    description="ETL dag",
    default_args=dag_args,
    schedule=timedelta(days=1),
    start_date=datetime(2021, 1, 1),
    catchup=False,
)

# inside container ETL path = /opt/airflow/ETL
extract_compose_file = "/opt/airflow/ETL/extract/docker-compose.yml"
transform_compose_file = "/opt/airflow/ETL/transform/docker-compose.yml"
load_compose_file = "/opt/airflow/ETL/load/docker-compose.yml"


extract_task = DockerOperator(
    task_id="ejecutar_extract",
    image="docker",
    api_version="auto",
    auto_remove=True,
    command="up --build",
    docker_url="unix://var/run/docker.sock",
    network_mode="bridge",
    volumes=[f"{extract_compose_file}:/docker-compose.yaml"],
    dag=dag,
)

transform_task = DockerOperator(
    task_id="ejecutar_transform",
    image="docker",
    api_version="auto",
    auto_remove=True,
    command="up --build",
    docker_url="unix://var/run/docker.sock",
    network_mode="bridge",
    volumes=[f"{transform_compose_file}:/docker-compose.yaml"],
    dag=dag,
)

load_task = DockerOperator(
    task_id="ejecutar_load",
    image="docker",
    api_version="auto",
    auto_remove=True,
    command="up --build --abort-on-container-exit",
    docker_url="unix://var/run/docker.sock",
    network_mode="bridge",
    volumes=[f"{load_compose_file}:/docker-compose.yaml"],
    dag=dag,
)

extract_task >> transform_task >> load_task
