import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder,MinMaxScaler
from data_handling import *
import config


class data_preprocessing:
    def __init__(self) -> None:
        self.data = data_handling.data_handling.read_test_data()
        print ("Data Preprocessing object created")
        print(self.data.head())

    def drop_columns(self, data, columns):
        data = data.drop(columns, axis = 1)
        return data

    def fillna(self, data, value):
        data = data.fillna(value)
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
    
    def preprocess_data_pipeline(self):
        print(self.data.head())
        return data
    
if __name__ == '__main__':
    preprocessing = data_preprocessing()
    data = preprocessing.preprocess_data_pipeline()
    print(data.head())


