
import pandas as pd
import os
os.chdir("/workspaces/iod-demo-repo/")

from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import utils
import argparse

def train_and_predict(dataset, model_name):
   
  config = utils.load_config()
     
  print("loading data for training...")
  
  # file_name = config[dataset]['input_file']['name']
  df = pd.read_csv(f"/workspaces/iod-demo-repo/artefacts/{dataset}.csv")   
      
  X_train, X_test, y_train, y_test = utils.split_train_test_data(df, config)
    
  if model_name == 'LogisticRegression':
      model = LogisticRegression()
  # elif model_name == 'SVC':
  #     model = SVC()
  elif model_name == 'GaussianNB':
      model = GaussianNB()
  else:
      raise ValueError(f"Unknown model: {model_name}")
  
  model.fit(X_train, y_train)
  y_pred = model.predict(X_test)
  print(accuracy_score(y_test, y_pred))
        
if __name__ == "__main__":
  
  parser = argparse.ArgumentParser(description="Train model with custom dataset and model")
    
  parser.add_argument("--dataset", required=True, help="dataset name")
  parser.add_argument("--model", required=True, help="model to train with")
  
  args = parser.parse_args()
  
  train_and_predict(args.dataset, args.model)
