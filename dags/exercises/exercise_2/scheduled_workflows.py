from datetime import datetime

from airflow import DAG
from airflow.operators.bash import BashOperator


# -------------------------
# Daily Sales DAG
# -------------------------
with DAG(
    dag_id="daily_sales",
    start_date=datetime(2026, 10, 1),
    schedule="0 9 * * *",
    catchup=False,
) as daily_sales:

    extract_sales = BashOperator(
        task_id="extract_sales",
        bash_command="echo 'Extracting daily sales data'",
    )

    process_sales = BashOperator(
        task_id="process_sales",
        bash_command="echo 'Processing daily sales data'",
    )

    generate_sales_report = BashOperator(
        task_id="generate_sales_report",
        bash_command="echo 'Generating daily sales report'",
    )

    extract_sales >> process_sales >> generate_sales_report


# -------------------------
# Weekly Customer Report DAG
# -------------------------
with DAG(
    dag_id="weekly_customer_report",
    start_date=datetime(2026, 10, 1),
    schedule="0 10 * * 1",
    catchup=False,
) as weekly_customer_report:

    collect_customer_data = BashOperator(
        task_id="collect_customer_data",
        bash_command="echo 'Collecting customer data'",
    )

    analyze_customers = BashOperator(
        task_id="analyze_customers",
        bash_command="echo 'Analyzing customer data'",
    )

    generate_customer_report = BashOperator(
        task_id="generate_customer_report",
        bash_command="echo 'Generating weekly customer report'",
    )

    collect_customer_data >> analyze_customers >> generate_customer_report
