import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder,MinMaxScaler
from sklearn.model_selection import train_test_split
from data_handling import *
import config
import os


class data_preprocessing(data_handling):
    def __init__(self):
        super().__init__()
        self.data = super().read_data_from ( config.PATH_OF_DATASET, config.TRAIN_DATA_NAME)
        print ("Data Preprocessing object created")
        # print(self.data.head())

    def drop_columns(self, data, columns):
        data = data.drop(columns, axis = 1)
        return data

    def handling_na(self, data, value = 0):
        data = data.dropna()
        data = data.reset_index(drop = True)
        return data

    def label_encode(self, data, columns):
        le = LabelEncoder()
        for col in columns:
            data[col] = le.fit_transform(data[col])
        return data

    def min_max_scale(self, data, columns):
        scaler = MinMaxScaler()
        for col in columns:
            data[col] = scaler.fit_transform(data[col].values.reshape(-1,1))
        return data

    def one_hot_encode(self, data, columns):
        data = pd.get_dummies(data, columns = columns)
        return data
    
    def train_test_split(self, data, test_size = 0.2):
        train, test = train_test_split(data, test_size = test_size, random_state = 142)
        return train, test
    
    def preprocess_data_pipeline(self):
        data = self.drop_columns(self.data, config.COLUMNS_DROP_BEFORE_PROCESSING)
        data = self.handling_na(data)
        data = self.label_encode(data, config.CATAGORICAL_COLUMNS)
        data = self.min_max_scale(data, config.COLUMNS_TRAIN_DATASET)

        train , test = self.train_test_split(data, config.TARIN_TEST_SPLIT_RATIO)
        super().save_processed_data(train, config.TRAIN_PROCESSED_DATA_NAME)
        super().save_processed_data(test, config.TEST_PROCESSED_DATA_NAME)

        return train
        
    
if __name__ == '__main__':
    preprocessing = data_preprocessing()
    data = preprocessing.preprocess_data_pipeline()
    print(data)
    # print(data.isna().sum())


