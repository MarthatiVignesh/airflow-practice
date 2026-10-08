from datetime import datetime

from airflow import DAG
from airflow.operators.bash import BashOperator


with DAG(
    dag_id="customer_pipeline",
    start_date=datetime(2026, 10, 1),
    schedule=None,
    catchup=False,
) as dag:

    start = BashOperator(
        task_id="start",
        bash_command="echo 'Starting customer pipeline'",
    )

    validate_data = BashOperator(
        task_id="validate_data",
        bash_command="echo 'Validating customer data'",
    )

    clean_data = BashOperator(
        task_id="clean_data",
        bash_command="echo 'Cleaning customer data'",
    )

    load_data = BashOperator(
        task_id="load_data",
        bash_command="echo 'Loading customer data'",
    )

    finish = BashOperator(
        task_id="finish",
        bash_command="echo 'Customer pipeline completed'",
    )

    start >> [validate_data, clean_data] >> load_data >> finish
