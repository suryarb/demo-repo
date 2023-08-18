import pandas as pd
import os
import yaml
from sklearn.model_selection import train_test_split

def load_config():

    print(f'loading config.yml...')
    
    os.chdir(r'/workspaces/iod-demo-repo/src')
    
    if os.path.exists("config.yml"):
        with open("config.yml", "r") as f:
            config = yaml.safe_load(f)
        return config
    else:
        return print("The config.yml file does not exist.")

def load_data(file_name):
        
    print(f'loading dataset {file_name}...')
    df = pd.read_csv(f'/workspaces/iod-demo-repo/DATA/{file_name}')

    return df

def split_train_test_data(df, config):
       
    for d in config:
        
        print(f'splitting train and test...')
        
        target_col = config[d]['target']
        feature_cols = [c for c in df.columns if c != target_col]
        
        X =  df[feature_cols]
        y = df[target_col]
   
    return train_test_split(X, y, test_size=0.2, random_state=1)