import pandas as pd
from pathlib import Path
import logging
import os
from sklearn.preprocessing import LabelEncoder, OrdinalEncoder, StandardScaler



log_dir = 'logs'
os.makedirs(log_dir, exist_ok=True)
# logging configuration
logger = logging.getLogger('data_pre-processing')
logger.setLevel('DEBUG')

console_handler = logging.StreamHandler()
console_handler.setLevel('DEBUG')

log_file_path = os.path.join(log_dir, 'data_pre-processing.log')
file_handler = logging.FileHandler(log_file_path)
file_handler.setLevel('DEBUG')

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.addHandler(console_handler)
logger.addHandler(file_handler)

def load_data(data: str) -> pd.DataFrame:
    try:
      Data = pd.read_csv(data)
      df = Data.drop(columns=['Patient_ID'], errors='ignore')
      logger.debug('data loaded from %s', data)    
      return df
    except pd.errors.ParserError as e:
       logger.error('error ouucur as %s', e)
       raise
    except ValueError as v:
       logger.error('error occur as %s', v) 
       raise 

import pandas as pd
from sklearn.preprocessing import LabelEncoder

def label_encoding(df):
    """
    Perform label encoding on specific categorical columns.
    """
    try:
        target = ['Gender', 'Smoking_Status', 'Allergies', 'Comorbidities']
        le = LabelEncoder()
        for col in target:
            if col in df.columns:
                df[col] = le.fit_transform(df[col].astype(str))
        logger.debug('Label encoding completed successfully!')
        return df
    except ValueError as v:
        logger.error('ValueError occurred: %s', v)
        raise
    except Exception as e:
        logger.error('Unexpected error occurred: %s', e)
        raise

def Ordinal_encoding(df):
    try:
        target2 = ['Air_Pollution_Level', 'Physical_Activity_Level', 'Occupation_Type', 'Asthma_Control_Level']
        Or = OrdinalEncoder()
        for col in target2:
            if col in df.columns:
                df[col] = Or.fit_transform(df[[col]].astype(str))
        logger.debug('Ordinal encoding completed successfully!')
        return df
    except ValueError as v:
        logger.error('ValueError occurred: %s', v)
        raise
    except Exception as e:
        logger.error('Unexpected error occurred: %s', e)
        raise

def standard_scaling(df):
    try:
        sc = StandardScaler()
        features = df.drop(columns=['Has_Asthma'], errors='ignore')
        df[features.columns] = sc.fit_transform(features)
        logger.debug('Standard scaling completed successfully!')
        return df
    except Exception as e:
        logger.error('Error in standard scaling: %s', e)
        raise

def save_data(df):
    try:
     folder_name = "Data"
     os.makedirs(folder_name, exist_ok=True)  # Create folder if it doesn't exist
     file_path = os.path.join(folder_name, "preprocesed_data.csv")
     df.to_csv(file_path, index=False)
     logger.debug('data saved !')
    except pd.errors.ParserError as e:
       logger.error('error ouucur as %s', e)
    except ValueError as v:
       logger.error('error occur as %s', v) 
       raise    

def main():
    df = load_data(r'C:\Users\wadood\Desktop\my personal proj\Data\clean_data.csv')
    label_encoding(df)
    Ordinal_encoding(df)
    standard_scaling(df)
    save_data(df)

main()
        
    




    







          
