import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import argparse
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

logger = logging.getLogger(__name__)

def apply_preprocessing(df, model, ds_config):
      
    for col, transform_type in ds_config['transform'].items():
        
        logger.debug(f'performing {transform_type} transformation on {col}...')
        
        if transform_type == 'MinMaxScaler':
            scaler = MinMaxScaler()
            df[[col]] = scaler.fit_transform(df[[col]])
            
        elif transform_type == 'log':
            scaler = MinMaxScaler()
            df[col] = np.log(df[col])
    
    return df

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description="Preprocessing")
    parser.add_argument("--df", required=True, help="data")
    parser.add_argument("--model", required=True, help="model to train with")
    parser.add_argument("--ds_config", required=True, help="dataset config")
    args = parser.parse_args()
    
    apply_preprocessing(args.model, args.ds_config)
    
    logger.debug('data preprocessing completed...')