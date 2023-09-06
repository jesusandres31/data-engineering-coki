from datetime import datetime, timedelta

from airflow.operators.bash_operator import BashOperator

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

# tasks
extract_task = BashOperator(
    task_id="extract_task",
    bash_command="docker-compose -f /opt/airflow/ETL/extract/docker-compose.yml up --build",
    dag=dag,
)

transform_task = BashOperator(
    task_id="transform_task",
    bash_command="docker-compose -f /opt/airflow/ETL/transform/docker-compose.yml up --build",
    dag=dag,
)

load_task = BashOperator(
    task_id="load_task",
    bash_command="docker-compose -f /opt/airflow/ETL/load/docker-compose.yml up --build --abort-on-container-exit",
    dag=dag,
)

# Define task dependencies as needed
extract_task >> transform_task >> load_task
