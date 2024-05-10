import os

TRAIN_DATA_NAME             = 'train.csv'
TEST_DATA_NAME              = 'test.csv'
TRAIN_PROCESSED_DATA_NAME   = 'train_processed.csv'
TEST_PROCESSED_DATA_NAME    = 'test_processed.csv'

TARIN_TEST_SPLIT_RATIO = 0.3

COLUMNS_DROP_BEFORE_PROCESSING = ["Loan_ID"]

CATAGORICAL_COLUMNS = ['Gender', 'Married', 'Dependents', 'Education', 'Self_Employed',\
                       'Property_Area', 'Loan_Status']

NUMERICAL_COLUMNS = ['ApplicantIncome', 'CoapplicantIncome', 'LoanAmount', \
                     'Loan_Amount_Term', 'Credit_History']


COLUMNS_TRAIN_DATASET = ['Gender', 'Married', 'Dependents', 'Education', 'Self_Employed',\
                        'ApplicantIncome', 'CoapplicantIncome', 'LoanAmount',\
                        'Loan_Amount_Term', 'Credit_History', 'Property_Area', 'Loan_Status']

Y_LABEL = 'Loan_Status'

MODEL_NAME = 'DecisionTreeClassifier'

if os.environ.get('MODEL_PATH') is not None:
    MODEL_PATH = os.environ.get('MODEL_PATH')
else:
    MODEL_PATH = 'models'

if os.environ.get('PATH_OF_DATASET') is not None:
    PATH_OF_DATASET = os.environ.get('PATH_OF_DATASET')
else:
    PATH_OF_DATASET = "data"

MODEL_RESULTS_FILE = f"{MODEL_NAME}_results.txt"
