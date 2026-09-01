import pandas as pd
from helper import load_config, create_parent_directory
from omegaconf import DictConfig

def read_data(config: DictConfig):
    return pd.read_csv(config.raw_data.path, index_col='date')

def feature_engineering(df: pd.DataFrame) -> pd.DataFrame:
    return df.assign(
        body=abs(df['open'] - df['close'])
    )

def save_processed_data(df: pd.DataFrame, config: DictConfig):
    create_parent_directory(config.interim.path)
    df.to_csv(config.interim.path, index=False)

def process_data():
    config = load_config()
    df = read_data(config)
    df = feature_engineering(df)

    save_processed_data(df, config)

if __name__ == "__main__":
    process_data()