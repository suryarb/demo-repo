import pandas as pd
import joblib
from sklearn.metrics import accuracy_score
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

logger = logging.getLogger(__name__)

def evaluate(model, ds_config):
    
    logger.debug(f"loading saved {model} model...")
    saved_model = joblib.load(f"/workspaces/demo-repo/models/{model}_{ds_config['name']}.joblib")
    
    X_test = pd.read_csv(f"/workspaces/demo-repo/artefacts/{model}_{ds_config['name']}_X_test.csv")
    y_test = pd.read_csv(f"/workspaces/demo-repo/artefacts/{model}_{ds_config['name']}_y_test.csv")
    y_pred = saved_model.predict(X_test)
    
    # saved_model.get_params()
    
    # logger.debug(f"{model} prameters: {saved_model.get_params()}")
    logger.debug(f"accuracy for {model}: {accuracy_score(y_test, y_pred)}")


if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description="Evaluate models")
    parser.add_argument("--model", required=True, help="model to train with")
    parser.add_argument("--ds_config", required=True, help="dataset config")
    
    args = parser.parse_args()
    evaluae(args.model, args.ds_config)
    
    logger.debug('data preparation completed...')