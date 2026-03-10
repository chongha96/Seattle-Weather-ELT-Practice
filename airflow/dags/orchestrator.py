import sys
from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator
from airflow.providers.docker.operators.docker import DockerOperator
from datetime import datetime, timedelta
from docker.types import Mount

sys.path.append('/opt/airflow/api-request')
from insert_records import main


default_args = {
    'description': 'A DAG to orchestrate data',
    'start_date':datetime(2026,3,9),
}

dag = DAG(
    dag_id='weather-api-dbt-orchestrator',
    default_args=default_args,
    #How often the program will run
    schedule=timedelta(minutes=60),
    catchup=False
)


with dag:
    task1 = PythonOperator(
        task_id='ingest_data_psql',
        python_callable = main
    )
    task2 = DockerOperator(
        task_id='transform_data_task',
        image='ghcr.io/dbt-labs/dbt-postgres:1.9.latest',
        command='run',
        working_dir='/usr/app',
        environment={
            'DBT_PROFILES_DIR':'/root/.dbt'
        },
        mounts=[
            Mount(source='/home/joshu/repos/weather-data-project/dbt/my_project',
                  target='/usr/app',
                  type='bind'),
            Mount(source='/home/joshu/repos/weather-data-project/dbt/profiles.yml',
                  target='/root/.dbt/profiles.yml',
                  type='bind'),                   
        ],
        network_mode='weather-data-project_my-network',
        docker_url='unix://var/run/docker.sock',
        auto_remove='success'
    )

    task1 >> task2