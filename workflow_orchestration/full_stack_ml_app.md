# Build a Full-Stack ML Application With Pydantic and Prefect

- Create a UI
- Validate Parameters

## How to run a function from a UI

1. Turn your function into a flow
2. Create a deployment
3. Start an agent to run the deployment

```python
from prefect import flow
from typing import List, Literal

@flow
def process(
    raw_localtion: Literal["data/raw", "data/processed"] = "data/raw",
    process_location: Literal["data/raw", "data/processed"] = "data/processed",
    columns_to_drop: List[str] = ["Id"]
)
    ...
```

Run Deployment

```bash
prefect deployment build process.py:process -n 'iris-process' -a
```

Run Agent

```bash
prefect agent start -q 'default'
```