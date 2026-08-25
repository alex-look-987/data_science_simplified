# Validate Python Tnput Values for a Machine Learning Application with Pydantic

```mermaid
%%{init: {'theme': 'base', 'themeVariables': { 'background': '#ffffff'}, {'lineColor: #fffbfb }}}%%
graph LR
    TS["Test Size: No idea"] --> Q{Is this a float?}
    Q -- Yes --> R[Run the flow]
    Q -- No --> E[Raises an error]

    style TS fill:#a3c2e0,stroke:#333,color:#000
    style Q fill:#e0c9a3,stroke:#333,color:#000
    style R fill:#a3d9c9,stroke:#333,color:#000
    style E fill:#f4b3b3,stroke:#333,color:#000
```

```mermaid
%%{init: {'theme': 'base', 'themeVariables': { 'background': '#ffffff'}}}%%
graph TB
    subgraph DL[DATA LOCATION]
        RF[Raw File]
        RL[Raw Location]
        PL[Process Location]
    end
    subgraph PC[PROCESS CONFIG]
        LB[Label]
        TS[Test Size]
        DC[Drop Columns]
    end

    style DL fill:#a3c2e0,stroke:#333,color:#000
    style PC fill:#c9c9c9,stroke:#333,color:#000
    style RF fill:#2b4fe0,stroke:#333,color:#fff
    style RL fill:#2b4fe0,stroke:#333,color:#fff
    style PL fill:#2b4fe0,stroke:#333,color:#fff
    style LB fill:#3a4a55,stroke:#333,color:#fff
    style TS fill:#3a4a55,stroke:#333,color:#fff
    style DC fill:#3a4a55,stroke:#333,color:#fff
```

## Pydantic

```python
from prefect import flow
from typing import List, Literal
from pydantic import BaseModel, validator

class DataLocation(BaseModel):
    raw_location: Literal["data/raw", "data/processed"] = "data/raw"
    raw_file: str = "iris.csv"
    process_location: Literal["data/raw", "data/processed"] = "data/processed"

class ProcessConfig(BaseModel):
    drop_columns: List[str] = ["Id"]
    label: str = "Species"
    test_size: float = 0.3

@flow
def process(
    data_location: DataLocation = DataLocation(),
    process_config: ProcessConfig = ProcessConfig()
):
    data = get_raw_dat(data_location.raw_location, data_location.raw_file)
    processed = drop_columns(data, process_config.drop_columns)
    X, y = get_X_y(processed, process_config.label)
    split_data = split_train_test(X, y, process_config.test_size)
    save_processed(split_data, data_location.process_location)

if __name__ = "__main__":
    process(test_size=0.4)
```

## Create Custom Validators

```python
from prefect import flow
from typing import List, Literal
from pydantic import BaseModel, validator

class ProcessConfig(BaseModel):
    drop_columns: List[str] = ["Id"]
    label: str = "Species"
    test_size: float = 0.3

    @validator("test_size")
    def must_be_non_negative(cls, v):
        if v < 0:
            raise ValueError(f"{v} must be non-negative")
        return v

if __name__ = "__main__":
    process(process_config=ProcessConfig(test_size=-0.5))


```