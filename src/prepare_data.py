import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import utils
import argparse

def clean_data(df, dataset, config):
    
    print(f'cleaning data...')
    if config[dataset]['input_file']['drop_cols'] is not None:
        df.drop(columns=config[dataset]['input_file']['drop_cols'], inplace=True)
        
    if config[dataset]['input_file']['drop_nulls'] is not None:
        df.dropna(subset=config[dataset]['input_file']['drop_nulls'], inplace=True)

    return df

def transform_target(df, dataset, config):
    
    bm_map = {
        'B': 0,
        'M': 1
        }
    
    df[config[dataset]['target']] = df[config[dataset]['target']].map(bm_map)

    return df

def prepare(dataset, model):
    
    config = utils.load_config()
    df = utils.load_data(config[dataset]['input_file']['name'])

    df = clean_data(df, dataset, config)
       
    if model =='SVC':
        df = transform_target(df, dataset, config)

    df.to_csv(f"/workspaces/iod-demo-repo/artefacts/{dataset}.csv", index=False)

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description="Train model with custom dataset and model")
    
    parser.add_argument("--dataset", required=True, help="dataset name")
    parser.add_argument("--model", required=True, help="model to train with")
    
    args = parser.parse_args()
    
    prepare(args.dataset, args.model)
    
    print("data preparation completed...")