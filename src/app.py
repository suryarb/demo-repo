import prepare_data
import train
import preprocess
import logging
import datetime
import pytz

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

logger = logging.getLogger(__name__)

if __name__ == "__main__":
    
    config = prepare_data.load_config()
    
    for dataset in config:
        
        ds_config = config[dataset]
        
        for model in ds_config['models']:
            
            logger.debug(f'preparing {dataset} dataset to train with {model}...')
            df = prepare_data.prepare(model, ds_config)
                        
            if 'transform' in ds_config:
                df = preprocess.apply_preprocessing(df, model, ds_config)

            train.train_and_predict(df, model, ds_config)
                           
        logger.debug(f'training and evaluation complete...')
        
        # add pca option from lab 6.4
