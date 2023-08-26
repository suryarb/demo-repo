import pandas as pd
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import prepare_data
import argparse
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def create_model(model_name):
    if model_name == 'LogisticRegression':
        return LogisticRegression()
    elif model_name == 'SVC':
        return SVC()
    elif model_name == 'GaussianNB':
        return GaussianNB()
    elif model_name == 'RandomForestClassifier':
        return RandomForestClassifier()
    else:
        raise ValueError(f"Unknown model: {model_name}")

def define_model(model_name, ds_config, df):
    
    grid_search = GridSearchCV(create_model(model_name), ds_config['models'][model_name]['cv'], cv=5)
    target_col = ds_config['target']
    feature_cols = [c for c in df.columns if c != target_col]
    
    X = df[feature_cols]
    y = df[target_col]
    grid_search.fit(X, y)
    
    # print("Best Parameters:", grid_search.best_params_)
    # print("Best Score:", grid_search.best_score_)
    
    return grid_search.best_params_, grid_search.best_score_

def train_and_predict(df, model_name, ds_config):
    logger.debug('loading prepared data for training...')

    model = create_model(model_name)
    
    if ds_config['models'][model_name] is None:
        model = create_model(model_name)
    elif 'cv' in ds_config['models'][model_name]:
        if 'params' not in ds_config['models'][model_name]:
            
            logger.debug('performing cross validation...')
            best_params, _ = define_model(model_name, ds_config, df)
            model.set_params(**best_params)
            logger.debug(f'best params {best_params}...')
        else:
            best_params = ds_config['models'][model_name]['params']
            model.set_params(**best_params)

    X_train, X_test, y_train, y_test = prepare_data.split_train_test_data(df, ds_config)

    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    
    result_df = pd.concat([X_test, y_test, pd.Series(y_pred, name='y_pred')], axis=1)
    result_df.to_csv(f"../outputs/{ds_config['name']}_results.csv", index=False)

    logger.debug(f"accuracy for {model}: {accuracy_score(y_test, y_pred)}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Train model with custom dataset and model")
    parser.add_argument("--df", required=True, help="data")
    parser.add_argument("--model", required=True, help="model to train with")
    parser.add_argument("--ds_config", required=True, help="dataset config")
    args = parser.parse_args()
    
    train_and_predict(args.model, args.ds_config)
