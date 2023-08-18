import pandas as pd
import os
import yaml
from sklearn.model_selection import train_test_split
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')


logger = logging.getLogger(__name__)

def load_config():

    logger.debug('loading config.yml...')
    
    os.chdir(r'/workspaces/iod-demo-repo/src')
    
    if os.path.exists("config.yml"):
        with open("config.yml", "r") as f:
            config = yaml.safe_load(f)
        return config
    else:
        return print("The config.yml file does not exist.")

def load_data(file_name):
        
    logger.debug(f'loading dataset {file_name}...')
    df = pd.read_csv(f'/workspaces/iod-demo-repo/DATA/{file_name}', index_col='id')

    return df

def split_train_test_data(df, config):
       
    for d in config:

        logger.debug(f'splitting train and test...')
        
        target_col = config[d]['target']
        feature_cols = [c for c in df.columns if c != target_col]
        
        X =  df[feature_cols]
        y = df[target_col]
   
    return train_test_split(X, y, random_state=1)