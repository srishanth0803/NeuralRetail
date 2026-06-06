from airflow import DAG
# pyrefly: ignore [missing-import]
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime

def ingest():
    print("Ingest Bronze")

def validate():
    print("Validate Data")

def notify():
    print("Pipeline Failed Notification")

with DAG(
    "retail_pipeline",
    start_date=datetime(2026,1,1),
    schedule="@daily",
    catchup=False
) as dag:

    ingest_task = PythonOperator(
        task_id="ingest_bronze",
        python_callable=ingest
    )

    validate_task = PythonOperator(
        task_id="validate_dq",
        python_callable=validate
    )

    notify_task = PythonOperator(
        task_id="notify_on_failure",
        python_callable=notify
    )

    ingest_task >> validate_task >> notify_task