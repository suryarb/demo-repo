
import pandas as pd
import os
os.chdir("/workspaces/demo-repo/")

from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import utils
import argparse
import joblib

import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

logger = logging.getLogger(__name__)

def train_and_predict(model_name, ds_config):
    
    logger.debug('loading prepared data for training...')
    
    df = pd.read_csv(f"/workspaces/demo-repo/artefacts/{ds_config['name']}.csv")       
    X_train, X_test, y_train, y_test = utils.split_train_test_data(df, ds_config)
    
    logger.debug(f'instantiating the {model_name} model...')
    if model_name == 'LogisticRegression':
        model = LogisticRegression(max_iter=5000)
    elif model_name == 'SVC':
        model = SVC()
    elif model_name == 'GaussianNB':
        model = GaussianNB()
    elif model_name == 'RandomForestClassifier':
        model = RandomForestClassifier(n_estimators=100, random_state=42)
    else:
        raise ValueError(f"Unknown model: {model_name}")
    
    logger.debug(f'fitting the {model_name} model...')
    model.fit(X_train, y_train)
    
    logger.debug(f'saving the fitted {model_name} model...')
    joblib.dump(model, f"/workspaces/demo-repo/models/{model_name}_{ds_config['name']}")
    
    y_pred = model.predict(X_test)
    
    logger.debug(f'calculating accuracy...{accuracy_score(y_test, y_pred)}')
        
if __name__ == "__main__":
  
  parser = argparse.ArgumentParser(description="Train model with custom dataset and model")
    
  parser.add_argument("--model", required=True, help="model to train with")
  parser.add_argument("--ds_config", required=True, help="dataset config")
  
  args = parser.parse_args()
  
  train_and_predict(args.model, args.ds_config)
