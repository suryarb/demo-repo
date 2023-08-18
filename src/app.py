import prepare_data
import train
import utils

import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

logger = logging.getLogger(__name__)

if __name__ == "__main__":
    
    config = utils.load_config()
    
    for dataset in config:
        
        ds_config = config[dataset]
        
        for model in ds_config['models']:
            
            logger.debug(f'preparing {dataset} to train with {model}...')
            
            prepare_data.prepare(model, ds_config)
            train.train_and_predict(model, ds_config)
    
            logger.debug(f'training complete...')
