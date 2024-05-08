PATH_OF_DATASET = "/home/safeer/Documents/ml/Ml_Models/ml_model_package/data"
TRAIN_DATA_NAME = 'train.csv'
TEST_DATA_NAME = 'test.csv'
TRAIN_PROCESSED_DATA_NAME = 'train_processed.csv'

COLUMNS_DROP_BEFORE_PROCESSING = ["Loan_ID"]

CATAGORICAL_COLUMNS = ['Gender', 'Married', 'Dependents', 'Education', 'Self_Employed',\
                       'Property_Area', 'Loan_Status']

NUMERICAL_COLUMNS = ['ApplicantIncome', 'CoapplicantIncome', 'LoanAmount', \
                     'Loan_Amount_Term', 'Credit_History']


COLUMNS_TRAIN_DATASET = ['Gender', 'Married', 'Dependents', 'Education', 'Self_Employed',\
                        'ApplicantIncome', 'CoapplicantIncome', 'LoanAmount',\
                        'Loan_Amount_Term', 'Credit_History', 'Property_Area', 'Loan_Status']

