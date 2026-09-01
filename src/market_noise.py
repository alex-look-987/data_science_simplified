import pandas as pd
import numpy as np
from helper import load_config, create_parent_directory
from omegaconf import DictConfig

def read_data(config: DictConfig):
    return pd.read_csv(config.interim.path)

def simulate_gaussian_noise(df: pd.DataFrame, config: DictConfig) -> pd.DataFrame:
    """Simulation market data variability adding gaussian noise
    
    Args:
        df (pd.DataFrame): _description_
        config (_type_): _description_

    Returns:
        pd.DataFrame: _description_
    """
    
    noise = np.random.normal(config.market_noise.loc, config.market_noise.scale, size=df.shape)

    return df + noise

def simulate_data_drift(df: pd.DataFrame, config: DictConfig) -> pd.DataFrame:
    """Simulates data drift distributiom between runs

    Args:
        df (pd.DataFrame): _description_
        config (DictConfig): _description_

    Returns:
        pd.DataFrame: _description_
    """

    shift = np.random.uniform(-config.market_noise.drift_factor, config.market_noise.drift_factor)

    return df * (2 + shift)

def save_processed_data(df: pd.DataFrame, config: DictConfig):
    create_parent_directory(config.processed.path)
    df.to_csv(config.processed.path, index=False)

def processed_market_noise():
    config = load_config()

    df = read_data(config)

    df = simulate_gaussian_noise(df, config)
    df = simulate_data_drift(df, config)

    save_processed_data(df, config)

if __name__ == "__main__":
    processed_market_noise()