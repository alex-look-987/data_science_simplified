# Build a Fully Automated Data Drift Detection Pipeline

```mermaid
%%{init: {'theme': 'base', 'themeVariables': { 'background': '#ffffff', 'lineColor': '#888888'}}}%%
graph TB
    PG1[Postgres database] --> RC[data/reference.csv]
    W[Web] --> CC[data/current.csv]
    RC --> DD[Detect dataset drift]
    CC --> DD
    RC --> PG2[Postgres database]
    CC --> PG2
    DD --> DDT[drift_detected]
    DDT --> STOP((Stop))
    DDT --> DO((Do the following))
    DO --> SL[Slack]
    DO --> RT[Retrain the model]
    RT --> MP[model.pkl]
    MP --> S3[S3 bucket]

    style PG1 fill:#a3c2e0,stroke:#333,color:#000
    style W fill:#a3c2e0,stroke:#333,color:#000
    style PG2 fill:#a3c2e0,stroke:#333,color:#000
    style SL fill:#a3c2e0,stroke:#333,color:#000
    style S3 fill:#a3c2e0,stroke:#333,color:#000
    style DD fill:#f4b3b3,stroke:#333,color:#000
    style RT fill:#f4b3b3,stroke:#333,color:#000
    style RC fill:#c9b3f4,stroke:#333,color:#000
    style CC fill:#c9b3f4,stroke:#333,color:#000
    style DDT fill:#c9b3f4,stroke:#333,color:#000
    style MP fill:#c9b3f4,stroke:#333,color:#000
    style STOP fill:#f4e0a3,stroke:#333,color:#000
    style DO fill:#f4e0a3,stroke:#333,color:#000
```

## Data Science Tasks

### Detect Data Drift

```mermaid
%%{init: {'theme': 'base', 'themeVariables': { 'background': '#ffffff', 'lineColor': '#888888'}}}%%
graph TB
    subgraph BG[ ]
        subgraph INPUTS[ ]
            RC[data/reference.csv]
            CC[data/current.csv]
        end
        RC --> DD[Detect dataset drift]
        CC --> DD
        DD --> DDT[drift_detected]
    end

    style RC fill:#c9b3f4,stroke:#333,color:#000
    style CC fill:#c9b3f4,stroke:#333,color:#000
    style DD fill:#f4b3b3,stroke:#333,color:#000
    style DDT fill:#c9b3f4,stroke:#333,color:#000
    style INPUTS fill:#ffffff,stroke:#3fd6d6
    style BG fill:#ffffff,stroke:#ffffff
```
```python
from evidently.metric_present_ import DataDriftPresent
from evidently.report import Report
from krestra import Kestra

data_drift_report = Report(metrics=[DataDriftPresent()])
data_drift_report.run(reference_data=reference, current_data=current)

report = data_drift_report.as_dict()
drift_detected = report['metrics'][0]['result']['dataset_drift']

if drift_detected:
    print("Detect dataset drift")
else:
    print("No dataset drift detected")

kestra.outputs({'drift_detected': drift_detected})
```

### Retrain Model

```mermaid
%%{init: {'theme': 'base', 'themeVariables': { 'background': '#ffffff', 'lineColor': '#888888'}}}%%
graph TB
    subgraph BG[ ]
        PC[Past and current data] --> RT[Retrain the model]
        RT --> MP[model.pkl]
    end

    style PC fill:#c9b3f4,stroke:#333,color:#000
    style RT fill:#f4b3b3,stroke:#333,color:#000
    style MP fill:#c9b3f4,stroke:#333,color:#000
    style BG fill:#ffffff,stroke:#ffffff
```

### Push to Github

```mermaid
%%{init: {'theme': 'base', 'themeVariables': { 'background': '#ffffff', 'lineColor': '#888888'}}}%%
graph TB
    subgraph BG[ ]
        DD[Detect dataset drift] --> GH[GitHub]
        RT[Retrain the model] --> GH
        GH --> BWF["Build workflows: allowing data engineers to use them in creating workflows"]
    end

    style DD fill:#f4b3b3,stroke:#333,color:#000
    style RT fill:#f4b3b3,stroke:#333,color:#000
    style GH fill:#a3c2e0,stroke:#333,color:#000
    style BWF fill:#f4e0a3,stroke:#333,color:#000
    style BG fill:#ffffff,stroke:#ffffff
```

## Data Engineering Tasks

### Airflow

```python
from datetime import datetime

from airflow import DAG
from airflow.decorators import task
from airflow.operators.bash import BashOperator

with DAG(dag_id='demo', start_date=datetime(2023, 7, 31), schedule='0 11 * * 1')
    my_task = BashOperator(
        task_id='someTask', bash_command='echo Hello'
    )

    # Developed inside the orchestration logic
    @task()
    def data_science_task():
            print('bye')

    # Set dependencies between tasks
    my_task >> data_science_tasks()
```

### Kestra

- Developed outside of the orchestration logic
- Incorporated into data workflws into YAML files
  
```bash
docker compose up -d
```

### Kestra YAML Orchestration file

[Data Drift Kestra Orchestration](data_drift/data_drift_kestra.yaml)

### Buidl a flow to send Slack Mesaages

[Slack Messages Kestra Automation](data_drift/send_slack_messages.yaml)

### Build a flow to retrain the modfel

[Retrain Model Flow](data_drift/retrain_model.yaml)