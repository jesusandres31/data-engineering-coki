# Apache Airflow

- Running Airflow in Docker would require to use DinD, so to avoid that we're gonna run Airflow just locally.

- IMPORTANT: if you're on Windows you must follow this stepts in a WSL terminal.

## install pip3

```
sudo apt-get install software-properties-common
sudo apt-add-repository universe
sudo apt-get update sudo apt-get install python3-pip
```

## create venv

```bash
# install
sudo apt install python3-virtualenv

# create
virtualenv venv

# run
source venv/bin/activate

# deactivate
deactivate
```

## create .env with Airflow path

```
export AIRFLOW_HOME=$(pwd)/airflow
echo "AIRFLOW_HOME=$(pwd)/airflow" >> .env
echo $AIRFLOW_HOME
```

## run airflow

airflow standalone

go to localhost:8080

## install airflow

https://airflow.apache.org/docs/apache-airflow/stable/start.html

IMPORTANT: instead of `export AIRFLOW_HOME=~/airflow` you would prefer `export AIRFLOW_HOME=$(pwd)/airflow`

<!--
## install airflow from pypi using pip

```
pip install apache-airflow
```

## initialize the database and default user

```
airflow db init
airflow users create -e admin@example.org -f John -l Doe -p admin -r Admin -u admin
airflow users list
```

## start the webserver

```bash
# default 8080
airflow webserver

# set port
airflow webserver -p 8081
```

## start the scheduler

```
airflow scheduler
```
-->
