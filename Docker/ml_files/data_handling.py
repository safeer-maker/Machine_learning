import os
import pandas as pd
import numpy as np
import config

class data_handling:
    def __init__(self):
        print ("Data Handling object created")
        self.path_test              = config.PATH_OF_DATASET
        self.path_train             = config.PATH_OF_DATASET
        self.path_train_processed   = config.PATH_OF_DATASET

    def get_path_variables(self):
        return {
            'path_test': self.path_test,
            'path_train': self.path_train,
            'path_train_processed': self.path_train_processed
        }

    def read_train_data(self, dataset_name = 'train.csv'):
        path = os.path.join(self.path_train, dataset_name)
        if not os.path.exists(path):
            print('File not found', path)
            return None
        else:
            print('File found at ', path)
            data = pd.read_csv(path)
            return data
    
    def read_test_data(self, dataset_name = 'test.csv'):
        path = os.path.join(self.path_test, dataset_name)
        if not os.path.exists(path):
            print('File not found', path)
            return None
        else:
            print('File found at ', path)
            data = pd.read_csv(path)
            return data
        
    def read_data_from (self, path ,dataset_name ):
        path = os.path.join(path, dataset_name)
        if not os.path.exists(path):
            print('File not found', path)
            return None
        else:
            print('File found at ', path)
            data = pd.read_csv(path)
            return data
        
    def read_train_processed_data(self, dataset_name = 'train_processed.csv'):
        path = os.path.join(self.path_train_processed, dataset_name)
        if not os.path.exists(path):
            print('File not found', path)
            return None
        else:
            print('File found at ', path)
            data = pd.read_csv(path)
            return data
        
    def read_train_processed_data_from(self, path, dataset_name ):
        path = os.path.join(self.path_train_processed, path, dataset_name)
        if not os.path.exists(path):
            print('File not found', path)
            return None
        else:
            print('File found at ', path)
            data = pd.read_csv(path)
            return data
    
    def save_processed_data (self, data, dataset_name = 'train_processed.csv', path = config.PATH_OF_DATASET ):
        path = os.path.join(self.path_train_processed, dataset_name)
        data.to_csv(path, index = False)
        print('Processed Data saved at ', path)
        return None
        

if __name__ == '__main__':
    dh = data_handling()
    print (dh.read_train_data())
    dh.read_data_from( config.PATH_OF_DATASET , config.TRAIN_DATA_NAME)
    # dh.read_test_data()
    # dh.read_train_processed_data()
    