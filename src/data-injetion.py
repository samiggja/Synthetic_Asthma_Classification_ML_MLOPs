import pandas as pd
from pathlib import Path
import logging
import os


log_dir = 'logs'
os.makedirs(log_dir, exist_ok=True)
# logging configuration
logger = logging.getLogger('data_ingestion')
logger.setLevel('DEBUG')

console_handler = logging.StreamHandler()
console_handler.setLevel('DEBUG')

log_file_path = os.path.join(log_dir, 'data_ingestion.log')
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
      df = Data.drop(columns=['Patient_ID'])
      logger.debug('data loaded from %s', data)    
      return df
    except pd.errors.ParserError as e:
       logger.error('error ouucur as %s', e)
       raise
    except ValueError as v:
       logger.error('error occur as %s', v) 
       raise    


def fill_NAN(df) -> pd.DataFrame:
   """""
   fill empty values from mode
   """
   try:
    df['Allergies'] = df['Allergies'].fillna(df['Allergies'].mode()[0])
    df['Comorbidities'] = df['Comorbidities'].fillna(df['Comorbidities'].mode()[0])
    df['Asthma_Control_Level'] = df['Asthma_Control_Level'].fillna(df['Asthma_Control_Level'].mode()[0])
    logger.debug('empty values are fillled with mode')
   except pd.errors.ParserError as e:
       logger.error('error ouucur as %s', e)
   except ValueError as v:
       logger.error('error occur as %s', v) 
       raise        
   

def save_data1(df):
    try:
     folder_name = "Data"
     os.makedirs(folder_name, exist_ok=True)  # Create folder if it doesn't exist
     file_path = os.path.join(folder_name, "clean_data.csv")
     df.to_csv(file_path, index=False)
     logger.debug('data saved !')
    except pd.errors.ParserError as e:
       logger.error('error ouucur as %s', e)
    except ValueError as v:
       logger.error('error occur as %s', v) 
       raise    

def main():
   df = load_data(r'C:\Users\wadood\Desktop\my personal proj\main_data\synthetic_asthma_dataset.csv') 
   fill_NAN(df)
   save_data1(df)  

main()   
