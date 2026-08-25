# Workflow Orchestration - Supercharge Your Data Pipeline in Python | Prefect

## Eliminate Negative Engineering wiht Prefect

### Machine Learning Pipeline

- Load Data > Process Data > Train Model > Make Prediction

### Positive Engineering

Focused entirely on writing the core logic that achieves the business goal 

### Negative Engineering

Extra defensive code and processes you must write to handle failures, erros and edge cases

### Prefect

- Open-source workflow orchestration
- Python-based
- Eliminate negative engineering

## Flow in Prefect

What is a Flow? 

- The basics of all Prefect workflows

### Functionalities of a Flow

1. Observability
2. Retries
3. Timeout
4. Effortlessly run your code concurrently or in parallel
5. Prerequisite to creating a deployment
    - Schedule
    - Send notifications

### How to turn your code into a Flow

```python

import pandas as pd
from prefect import flow

@flow
def process_data():
    ...

```

## Tasks in Prefect

```mermaid
%%{init: {'theme': 'base', 'themeVariables': { 'background': '#ffffff'}}}%%
graph LR
    A{{Flow 1}} --> B[Task 1]
    A --> C[Task 2]
    A --> D[Task 3]

    style A fill:#c8e6c9,stroke:#333,color:#000
    style B fill:#ffffff,stroke:#999,color:#000
    style C fill:#e57373,stroke:#333,color:#000
    style D fill:#ffffff,stroke:#999,color:#000
```

```mermaid
%%{init: {'theme': 'base', 'themeVariables': { 'background': '#ffffff'}}}%%
graph TD
    A[Task runners] --> B[Sequential]
    A --> C[Concurrent]
    A --> D[Parallel]
    D --> E[Dask]
    D --> F[Ray]

    style A fill:#b39ddb,stroke:#333,color:#000
    style B fill:#f9dcb4,stroke:#333,color:#000
    style C fill:#f9dcb4,stroke:#333,color:#000
    style D fill:#f9dcb4,stroke:#333,color:#000
    style E fill:#a8d5e5,stroke:#333,color:#000
    style F fill:#a8d5e5,stroke:#333,color:#000
```

```python

from prefect import task

@task
def load_config(
    with initialize(version_base=None, config_path='../config')
        config = compose(config_name='main')

    return config
)

```

## Observe Data Pipelines through Prefect Orion Server

### View flow runs through Prefect UI

```mermaid
%%{init: {'theme': 'base', 'themeVariables': { 'background': '#ffffff'}}}%%
graph TD
    A[Prefect UI] --> B[Prefect Orion Server]
    A --> C[Prefect Cloud]
    B --> D[Open source]
    B --> E[Locally hosted]
    C --> F[Hosted service]
    C --> G[Collaborators]
    C --> H[Personal accounts]
    C --> I[Workspaces]

    style A fill:#b3b3e0,stroke:#333,color:#000
    style B fill:#e0a3a3,stroke:#333,color:#000
    style C fill:#e0a3a3,stroke:#333,color:#000
    style D fill:#c3e0a3,stroke:#333,color:#000
    style E fill:#c3e0a3,stroke:#333,color:#000
    style F fill:#c3e0a3,stroke:#333,color:#000
    style G fill:#c3e0a3,stroke:#333,color:#000
    style H fill:#c3e0a3,stroke:#333,color:#000
    style I fill:#c3e0a3,stroke:#333,color:#000
```

### Functionalities of Prefect UI

- Flow run summaries
- Task run details
- Flow and task dependency visualizer
- Logs

```bash
prefect orion start
```

## Subflows in Prefect: Organize Data Pipelines in Python

```python
from prefect import flow

@flow
def prepare_for_training():
    ...

@flow
def train():
    ...

@flow
def development():
    prepare_for_training()
    train()
```

### Flow and Subflow

```mermaid
%%{init: {'theme': 'base', 'themeVariables': { 'background': '#ffffff'}}}%%
graph TD
    A[Development] --> B[Get Data]
    A --> C[Process data]
    A --> D[Train model]
    E[Production] --> F[Make prediction]

    style A fill:#a3c2e0,stroke:#333,color:#000
    style B fill:#f4b3b3,stroke:#333,color:#000
    style C fill:#a3d9c9,stroke:#333,color:#000
    style D fill:#e0c9a3,stroke:#333,color:#000
    style E fill:#a3c2e0,stroke:#333,color:#000
    style F fill:#e0c3e0,stroke:#333,color:#000
```

### Subflows or tasks

#### Use tasks when run tasks concurrently

```mermaid
%%{init: {'theme': 'base', 'themeVariables': { 'background': '#ffffff'}}}%%
gantt
    title Run tasks concurrently (CPU)
    dateFormat X
    axisFormat %s

    section Task 1
    Run : 0, 3
    Run : 5, 3

    section Task 2
    Run : 2, 3
    Run : 6, 2
```

#### Use flows when

```mermaid
%%{init: {'theme': 'base', 'themeVariables': { 'background': '#ffffff'}}}%%
graph TD
    A[Development] --> B[Get Data]
    A --> C[Process data]
    A --> D[Train model]
    B --> E[Sequential task runner]
    C --> F[Concurrent task runner]
    D --> G[Dask task runner]

    style A fill:#a3c2e0,stroke:#333,color:#000
    style B fill:#f4b3b3,stroke:#333,color:#000
    style C fill:#a3d9c9,stroke:#333,color:#000
    style D fill:#e0c9a3,stroke:#333,color:#000
    style E fill:#c3e0a3,stroke:#333,color:#000
    style F fill:#c3e0a3,stroke:#333,color:#000
    style G fill:#c3e0a3,stroke:#333,color:#000
```

```mermaid
%%{init: {'theme': 'base', 'themeVariables': { 'background': '#ffffff'}}}%%
graph LR
    A{Subflow 1} --> B[Deployment 1]
    C{Subflow 2} --> D[Deployment 2]
    E{Subflow 3} --> F[Deployment 3]

    style A fill:#c3e0a3,stroke:#333,color:#000
    style B fill:#a3c2e0,stroke:#333,color:#000
    style C fill:#c3e0a3,stroke:#333,color:#000
    style D fill:#a3c2e0,stroke:#333,color:#000
    style E fill:#c3e0a3,stroke:#333,color:#000
    style F fill:#a3c2e0,stroke:#333,color:#000
```

## Caching Your Python Functions

```mermaid
%%{init: {'theme': 'base', 'themeVariables': { 'background': '#ffffff'}}}%%
graph LR
    GD["GET DATA - 0.1s - Completed"] --> C["CACHED: FILL MISSING DESCRIPTION - 0s"]
    C --> GDL["GET DESCRIPTION LENGTH - 0.1s - Completed"]

    style GD fill:#a3d9c9,stroke:#333,color:#000
    style C fill:#e0c3e0,stroke:#333,color:#000
    style GDL fill:#a3d9c9,stroke:#333,color:#000
```

```python
from prefect import task

@task(cache_key_fn=task_input_hash, cache_expiration=...)
def load_config()
    ...
```

## Retries in Python: Rerun Failed Functions for a Specific Number of Times 

```python
from prefect import task

@task(retries=..., retry_delay_seconds=...)
def load_config()
    ...

```

## Schedule your Data Workflow

## Deploy a Data Pipeline (Part 1) - What is a Deployment

- Encapsulates a flow
- Allows it to be triggered via API

### Why Deployment

1. Turn a flow into an API
2. Specify infrastructure
3. Specify storage
4. Specify custom names/parameters in the UI
5. Schedule the flow run
6. Retry flow

```mermaid
%%{init: {'theme': 'base', 'themeVariables': { 'background': '#ffffff'}}}%%
graph TB
    D[Deployment]
    FC[Flow code] --> D
    N[Name] --> D
    I[Infrastructure] --> D
    WQ[Work queue] --> D
    P[Parameters] --> D
    S[Schedule] --> D
    E[Entrypoint] --> D
    ST[Storage] --> D

    style D fill:#333,stroke:#333,color:#fff
    style FC fill:#a3c2e0,stroke:#333,color:#000
    style N fill:#a3c2e0,stroke:#333,color:#000
    style I fill:#a3c2e0,stroke:#333,color:#000
    style WQ fill:#a3c2e0,stroke:#333,color:#000
    style P fill:#a3c2e0,stroke:#333,color:#000
    style S fill:#a3c2e0,stroke:#333,color:#000
    style E fill:#a3c2e0,stroke:#333,color:#000
    style ST fill:#a3c2e0,stroke:#333,color:#000
```

## Deploy a Data Pipeline (Part 3) - Create a Deployment

### How to deploy a flow

- Through a Python object
- Through a CLI

```mermaid
%%{init: {'theme': 'base', 'themeVariables': { 'background': '#ffffff'}}}%%
graph LR
    FC1[Flow code] --> FC2[Flow code]
    FC2 --> PA[Prefect API: Deployment]
    FC2 --> ST[Storage: Flow]
    PA --> AG[Agent]
    ST --> AG
    AG --> INF[Infrastructure: Flow run]

    style FC1 fill:#a3c2e0,stroke:#333,color:#000
    style FC2 fill:#a3c2e0,stroke:#333,color:#000
    style PA fill:#e0c9a3,stroke:#333,color:#000
    style ST fill:#a3d9c9,stroke:#333,color:#000
    style AG fill:#f4b3b3,stroke:#333,color:#000
    style INF fill:#e0c3e0,stroke:#333,color:#000
```

```mermaid
%%{init: {'theme': 'base', 'themeVariables': { 'background': '#ffffff'}}}%%
graph LR
    B[1: prefect deployment build] --> Y[creates deployments.yaml]
    B -.-> U[uploads flow code to remote storage]
    A[2: prefect deployment apply] --> C[creates deployment]

    style B fill:#a3c2e0,stroke:#333,color:#000
    style A fill:#a3c2e0,stroke:#333,color:#000
    style Y fill:#e0c9a3,stroke:#333,color:#000
    style U fill:#e0c9a3,stroke:#333,color:#000
    style C fill:#e0c9a3,stroke:#333,color:#000
```

```bash
prefect deployment build [OPTIONS]
<path-to-your-flow>:<flow-name> -n <name-of-deployment> -a (apply option)

prefect deployment apply <name-of-deployment-yaml-file>
```

## Deploy a Data Pipeline (Part 3) - Run a Deployment

- Work Queue
- Agents

```mermaid
%%{init: {'theme': 'base', 'themeVariables': { 'background': '#ffffff'}}}%%
graph TB
    A1[Agent 1] --> DQ[DEV WORK QUEUE]
    A2[Agent 2] --> PQ[PROD WORK QUEUE]
    DQ --> D1[1st Deployment 1]
    DQ --> D2[2nd Deployment 2]
    DQ --> D3[3rd Deployment 3]
    PQ --> D4[1st Deployment 4]
    PQ --> D5[2nd Deployment 5]
    PQ --> D6[3rd Deployment 6]

    style A1 fill:#a3c2e0,stroke:#333,color:#000
    style A2 fill:#a3c2e0,stroke:#333,color:#000
    style DQ fill:#a3d9c9,stroke:#333,color:#000
    style PQ fill:#e0c9a3,stroke:#333,color:#000
    style D1 fill:#f4b3b3,stroke:#333,color:#000
    style D2 fill:#f4b3b3,stroke:#333,color:#000
    style D3 fill:#f4b3b3,stroke:#333,color:#000
    style D4 fill:#e0c3e0,stroke:#333,color:#000
    style D5 fill:#e0c3e0,stroke:#333,color:#000
    style D6 fill:#e0c3e0,stroke:#333,color:#000
```

```mermaid
%%{init: {'theme': 'base', 'themeVariables': { 'background': '#ffffff'}}}%%
graph LR
    P[Python script] --> F[Create a flow]
    F --> UI[Prefect UI]
    UI --> DEP[Create a deployment]
    DEP --> WQ[Create a work queue]
    WQ --> AG[Start an agent]

    style P fill:#e0c9a3,stroke:#333,color:#000
    style F fill:#a3d9c9,stroke:#333,color:#000
    style UI fill:#f4b3b3,stroke:#333,color:#000
    style DEP fill:#a3d9c9,stroke:#333,color:#000
    style WQ fill:#e0c9a3,stroke:#333,color:#000
    style AG fill:#f4b3b3,stroke:#333,color:#000
```

```bash
prefect agent start -q 'default'

```

