import os
import pandas as pd
import numpy as np

class data_handling:
    def __init__(self) -> None:
        self.path_test = os.environ.get('PATH_TEST')
        self.path_train = os.environ.get('PATH_TRAIN')
        self.path_train_processed = os.environ.get('PATH_TRAIN_PROCESSED')

    def read_train_data(self, dataset_name = 'train.csv'):
        path = os.path.join(self.path_train, dataset_name)

        if not os.path.exists(path):
            print('File not found')
            return None
        else:
            print('File found at ', path)
            data = pd.read_csv(path)
            return data
    
    def read_test_data(self, dataset_name = 'test.csv'):
        path = os.path.join(self.path_test, dataset_name)
        if not os.path.exists(path):
            print('File not found')
            return None
        else:
            print('File found at ', path)
            data = pd.read_csv(path)
            return data
        
    def read_train_data_from(self, path ,dataset_name ):
        path = os.path.join(self.path_train,path, dataset_name)
        if not os.path.exists(path):
            print('File not found')
            return None
        else:
            print('File found at ', path)
            data = pd.read_csv(path)
            return data
        data = pd.read_csv(path)

    def read_train_processed_data(self, dataset_name = 'train_processed.csv'):
        path = os.path.join(self.path_train_processed, dataset_name)
        if not os.path.exists(path):
            print('File not found')
            return None
        else:
            print('File found at ', path)
            data = pd.read_csv(path)
            return data
        
    def read_train_processed_data_from(self, path, dataset_name ):
        path = os.path.join(self.path_train_processed, path, dataset_name)
        if not os.path.exists(path):
            print('File not found')
            return None
        else:
            print('File found at ', path)
            data = pd.read_csv(path)
            return data
    
    def save_train_processed_data(self, data, dataset_name = 'train_processed.csv'):
        path = os.path.join(self.path_train_processed, dataset_name)
        data.to_csv(path, index = False)
        print('Data saved at ', path)
        

if __name__ == '__main__':
    dh = data_handling()
    dh.read_train_data( 'tra.csv')
    dh.read_test_data()
    dh.read_train_data_from(r"/home/safeer/Documents/ml/Ml_Models", 'tra.csv')
    dh.read_train_processed_data()
    dh.save_train_processed_data(pd.DataFrame({'A':[1,2,3], 'B':[4,5,6]}))
