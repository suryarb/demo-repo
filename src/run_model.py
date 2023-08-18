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
        
        for model in config[dataset]['models']:
            
            logger.debug(f'preparing {dataset} to train with {model}...')
            
            prepare_data.prepare(dataset, model)
            train.train_and_predict(dataset, model)
    
            logger.debug(f'training complete...')
