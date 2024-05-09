import config
from sklearn.tree import *
from data_handling import *
import pandas as pd
import numpy as np
from joblib import dump, load

class model_training_inferancing(data_handling):
    def __init__(self):
        super().__init__()
        self.train_df = super().read_data_from (config.PATH_OF_DATASET, config.TRAIN_PROCESSED_DATA_NAME)
        self.test_df  = super().read_data_from (config.PATH_OF_DATASET, config.TEST_PROCESSED_DATA_NAME)
        self.train_X = pd.DataFrame([])
        self.test_X  = pd.DataFrame([])
        self.train_y = pd.DataFrame([])
        self.test_y  = pd.DataFrame([])
        model = None
        print ("Model Training object created")

    def get_X_y(self, data):
        X = data.drop(config.Y_LABEL, axis = 1)
        y = data['Loan_Status']
        return X, y
    
    def get_train_test_X_y(self):
        self.train_X, self.train_y = self.get_X_y(self.train_df)
        self.test_X, self.test_y = self.get_X_y(self.test_df)
        return None
    
    def train_model(self):
        self.model = DecisionTreeClassifier()
        self.model.fit(self.train_X, self.train_y)
        return self.model
    
    def save_model(self, model, model_name):
        path = os.path.join(config.MODEL_PATH, config.MODEL_NAME, "pkl")
        dump(model, path)
        print("Model saved at ", path)
        return None

    def load_model(self,):
        path = os.path.join(config.MODEL_PATH, config.MODEL_NAME, "pkl")
        self.model = load(path)
        return None

    def inferance(self, model, data):
        pass
    
    def model_score(self ):
        pass