import pandas as pd
import numpy as np
import argparse
import logging
import os
import yaml
from sklearn.model_selection import train_test_split

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

logger = logging.getLogger(__name__)

def load_config():

    logger.debug('loading config.yml...')
    
    os.chdir(r'/workspaces/demo-repo/src')
    
    # read config
    if os.path.exists("config.yml"):
        with open("config.yml", "r") as f:
            config = yaml.safe_load(f)
        return config
    else:
        return print("The config.yml file does not exist.")
    
def load_data(ds_config):
    
    logger.debug(f"loading dataset {ds_config['input_file']['name']}...")

    # read data
    if ds_config.get('input_file', {}).get('id_col') is not None:
        df = pd.read_csv(
            f"{ds_config['input_file']['path']}/{ds_config['input_file']['name']}",
            index_col=ds_config['input_file']['id_col']
        )
    else:
        df = pd.read_csv(f"{ds_config['input_file']['path']}/{ds_config['input_file']['name']}")

    return df

def split_train_test_data(df, ds_config):

    logger.debug(f'splitting train and test...')
    
    target_col = ds_config['target']
    feature_cols = [c for c in df.columns if c != target_col]
    
    X =  df[feature_cols]
    y = df[target_col]
   
    return train_test_split(X, y, random_state=1)

def clean_data(df, ds_config):
    
    # convert all columns to lower case
    logger.debug('convert all column names to lowercase...')
    df.columns = df.columns.str.lower()
    
    # rename columns
    if ds_config.get('input_file', {}).get('rename_cols') is not None:    
        rename_mapping = ds_config['input_file']['rename_cols']
        
        for old_name, new_name in rename_mapping.items():
            if old_name in df.columns:
                logger.debug(f'renaming column {old_name} to {new_name}...')
                df.rename(columns={old_name: new_name}, inplace=True)
    
    df.columns = df.columns.str.replace('[\.\s\[\]\(\)]', '_', regex=True)

    # drop columns
    if ds_config.get('input_file', {}).get('drop_cols') is not None:
        logger.debug(f"dropping columns {ds_config['input_file']['drop_cols']}...")
        df.drop(columns=ds_config['input_file']['drop_cols'], inplace=True)

    # drop nulls
    if ds_config.get('input_file', {}).get('drop_nulls') is not None:
        logger.debug(f"dropping NaN from {ds_config['input_file']['drop_nulls']}...")
        df.dropna(subset=ds_config['input_file']['drop_nulls'], inplace=True)

    return df

def transform_target(df, ds_config):
    
    bm_map = {
        'B': 0,
        'M': 1
        }
    
    df[ds_config['target']] = df[ds_config['target']].map(bm_map)

    return df

def prepare(model, ds_config):
    
    df = load_data(ds_config)
    df = clean_data(df, ds_config)
       
    if model =='SVC':
        df = transform_target(df, ds_config)

    return df

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description="Train model with custom dataset and model")
    parser.add_argument("--model", required=True, help="model to train with")
    parser.add_argument("--ds_config", required=True, help="dataset config")
    
    args = parser.parse_args()
    prepare(args.model, args.ds_config)
    
    logger.debug('data preparation completed...')