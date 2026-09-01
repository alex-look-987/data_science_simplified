from hydra import compose, initialize

def load_config():
    """Load configurations from the file 'main.yaml' under the 'config' dir"""

    with initialize(version_base=None, config_path='../config'):
        config = compose(config_name="main")

    return config

