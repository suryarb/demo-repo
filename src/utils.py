import pandas as pd
import os
import yaml

def load_config():

    os.chdir(r'/workspaces/iod-demo-repo/src')
    
    if os.path.exists("config.yml"):
        with open("config.yml", "r") as f:
            config = yaml.safe_load(f)
            print("The config.yml file read was successful.")
        return config
    else:
        return print("The config.yml file does not exist.")

def load_data(config):

    datasets = {}

    for d in config['datasets']:

        df = pd.read_csv('/workspaces/iod-demo-repo/DATA/' + d['input_files']['input_file_name'])
        # , names=['date', 'transaction_amount', 'merchant', 'none']

        df = df.assign(file_name=d['input_files']['input_file_name'])
        # df = df[d['input_files']['input_file_cols']]

        # df.to_csv('/workspaces/iod-demo-repo/output/'+ d['file_name'])

        datasets[str(d['name'])] = df

    return datasets