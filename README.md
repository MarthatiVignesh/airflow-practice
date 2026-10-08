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
│       └── exercise_1/
│           └── hello_workflow.py
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

## DAG ID

```text
hello_workflow
```

## Testing

The DAG was tested successfully using:

```bash
airflow dags test hello_workflow 2026-10-08
```

All tasks completed successfully and the DAG run finished with:

```text
state=success
```

## Airflow UI

Airflow Webserver:

```text
http://localhost:8080
```

The DAG can be viewed and triggered from the Airflow web interface.

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
