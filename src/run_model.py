import prepare_data
import train
import utils

if __name__ == "__main__":
    
    config = utils.load_config()
    
    for dataset in config:
        
        for model in config[dataset]['models']:
            
            print(f'preparing {dataset} to train with {model}...')
            
            prepare_data.prepare(dataset, model)
            train.train_and_predict(dataset, model)
    
    print("training complete...")