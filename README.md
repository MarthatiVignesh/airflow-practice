# Apache Airflow Practice

This repository contains my hands-on practice and exercises for **Apache Airflow** as part of my Data Engineering learning.

## Environment

- OS: Ubuntu / WSL2
- Python: 3.10.12
- Apache Airflow: 2.10.3
- Database: SQLite
- Executor: LocalExecutor

## Project Structure

```text
airflow-practice/
│
├── dags/
│   └── exercises/
│       ├── exercise_1/
│       │   └── hello_workflow.py
│       ├── exercise_2/
│       │   └── scheduled_workflows.py
│       ├── exercise_3/
│       │   └── customer_pipeline.py
│       └── exercise_4/
│           └── etl_ui_practice.py
│
├── docs/
│   └── screenshots/
│       ├── exercise_1/
│       │   ├── airflow-dag-list.png
│       │   └── airflow-graph.png
│       ├── exercise_2/
│       │   ├── airflow-dag-list.png
│       │   ├── daily-sales-graph.png
│       │   └── weekly-customer-report-graph.png
│       ├── exercise_3/
│       │   ├── airflow-dag-list.png
│       │   ├── customer-pipeline-graph.png
│       │   └── customer-pipeline-run.png
│       └── exercise_4/
│           ├── airflow-dag-list.png
│           ├── etl-graph.png
│           ├── etl-run.png
│           └── etl-task-details.png
│
└── README.md
```

## Exercise 1 - Hello Workflow

The first Airflow DAG demonstrates a simple sequential workflow.

### DAG Flow

```text
Start
  ↓
Student Name
  ↓
Course Name
  ↓
End
```

### Tasks

1. `start` - Starts the workflow
2. `student_name` - Displays the student name
3. `course_name` - Displays the course name
4. `end` - Completes the workflow

### DAG ID

```text
hello_workflow
```

### Testing

The DAG was tested successfully using:

```bash
airflow dags test hello_workflow 2026-10-08
```

All tasks completed successfully and the DAG run finished with:

```text
state=success
```

## Exercise 2 - Scheduled Workflows

Exercise 2 demonstrates how to create Airflow DAGs with schedules.

### 1. Daily Sales

**DAG ID:** `daily_sales`

### DAG Flow

```text
Extract Sales
      ↓
Process Sales
      ↓
Generate Sales Report
```

**Schedule:** Every day at 9:00 AM

### Tasks

1. `extract_sales` - Extracts daily sales data
2. `process_sales` - Processes daily sales data
3. `generate_sales_report` - Generates the daily sales report

### 2. Weekly Customer Report

**DAG ID:** `weekly_customer_report`

### DAG Flow

```text
Collect Customer Data
        ↓
Analyze Customers
        ↓
Generate Customer Report
```

**Schedule:** Every Monday at 10:00 AM

### Tasks

1. `collect_customer_data` - Collects customer data
2. `analyze_customers` - Analyzes customer data
3. `generate_customer_report` - Generates the weekly customer report

### Exercise 2 Testing

Both DAGs were tested successfully using:

```bash
airflow dags test daily_sales 2026-10-08
airflow dags test weekly_customer_report 2026-10-08
```

Both DAG runs completed with:

```text
state=success
```

## Exercise 3 - Customer Pipeline

Exercise 3 demonstrates a customer data pipeline with **parallel task execution**.

### DAG Flow

```text
             ┌──→ Validate Data ──┐
Start ───────┤                    ├──→ Load Data ──→ Finish
             └──→ Clean Data ─────┘
```

### DAG ID

```text
customer_pipeline
```

### Tasks

1. `start` - Starts the customer pipeline
2. `validate_data` - Validates customer data
3. `clean_data` - Cleans customer data
4. `load_data` - Loads the processed customer data
5. `finish` - Completes the customer pipeline

### Task Dependencies

The `validate_data` and `clean_data` tasks run in parallel after `start`. Both tasks must complete before `load_data` runs.

```text
start
  │
  ├──→ validate_data ──┐
  │                    ├──→ load_data ──→ finish
  └──→ clean_data ─────┘
```

### Testing

The DAG was tested successfully using:

```bash
airflow dags test customer_pipeline 2026-10-08
```

All tasks completed successfully and the DAG run finished with:

```text
state=success
```

## Exercise 4 - ETL UI Practice

Exercise 4 demonstrates a simple ETL workflow and practice with the Airflow UI.

### DAG Flow

```text
Extract
  ↓
Transform
  ↓
Load
  ↓
Notify
```

### DAG ID

```text
etl_ui_practice
```

### Tasks

1. `extract` - Extracts data
2. `transform` - Transforms data
3. `load` - Loads data
4. `notify` - Notifies that the ETL process completed successfully

### Testing

The DAG was tested successfully using:

```bash
airflow dags test etl_ui_practice 2026-10-08
```

All four tasks completed successfully and the DAG run finished with:

```text
state=success
```

### Airflow UI Practice

The exercise includes screenshots of:

- DAG list
- ETL graph
- Successful DAG run
- Task details

## Airflow UI

Airflow Webserver:

```text
http://localhost:8080
```

The DAGs can be viewed and triggered from the Airflow web interface.

## Learning Topics

This practice repository will cover:

- DAGs
- Tasks
- Task dependencies
- BashOperator
- Scheduling
- Parallel execution
- XCom
- Variables
- Connections
- Sensors
- Branching
- TaskFlow API
- Dynamic Task Mapping
- Retries and failure handling
- Backfill and rerun
- Airflow UI

## Author

**Vignesh**

Data Engineering Student
