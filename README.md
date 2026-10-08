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
│       └── exercise_2/
│           └── scheduled_workflows.py
│
├── docs/
│   └── screenshots/
│       └── exercise_1/
│           ├── airflow-dag-list.png
│           └── airflow-graph.png
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
