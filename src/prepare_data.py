import pandas as pd
import numpy as np
import utils
import argparse
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

logger = logging.getLogger(__name__)

def clean_data(df, ds_config):
    
    logger.debug('convert all column names to lowercase...')
    
    df.columns = df.columns.str.lower()
    
    if ds_config.get('input_file', {}).get('drop_cols') is not None:
        logger.debug(f"dropping columns {ds_config['input_file']['drop_cols']}...")
        df.drop(columns=ds_config['input_file']['drop_cols'], inplace=True)

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
    
    df = utils.load_data(ds_config)
    df = clean_data(df, ds_config)
       
    if model =='SVC':
        df = transform_target(df, ds_config)

    df.to_csv(f"/workspaces/iod-demo-repo/artefacts/{ds_config['name']}.csv", index=False)

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description="Train model with custom dataset and model")
    parser.add_argument("--model", required=True, help="model to train with")
    parser.add_argument("--ds_config", required=True, help="dataset config")
    
    args = parser.parse_args()
    prepare(args.model, args.ds_config)
    
    logger.debug('data preparation completed...')