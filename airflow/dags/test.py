from datetime import datetime, timedelta

from airflow.exceptions import AirflowFailException
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

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
    description="My first DAG",
    default_args=dag_args,
    schedule=timedelta(days=1),  # you can use cron here to schedule
    start_date=datetime(2021, 1, 1),
    catchup=False,
    tags=["example"],
    params={"commit": "000000"},
)


def task0_func():
    with open("/opt/airflow/dags/file.txt", "w") as file:
        file.write("Hello, this is a sample text file created by Airflow!")
        print("File created successfully")


def task2_func(**kwargs):
    xcom_value = kwargs["ti"].xcom_pull(task_ids="task0")

    print("Hello")
    print(xcom_value)

    return {"ok": "task2 ok"}


task0 = PythonOperator(task_id="task0", python_callable=task0_func, dag=dag)

task1 = BashOperator(
    task_id="bash_func",
    bash_command="ls /opt/airflow/code && pwd",
    dag=dag,
)

task2 = PythonOperator(task_id="task2", python_callable=task2_func, dag=dag)

task0 >> task1 >> task2
