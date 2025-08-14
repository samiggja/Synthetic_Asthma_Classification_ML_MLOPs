import logging
import os
import pickle
import pandas as pd

log_dir = 'logs'
os.makedirs(log_dir, exist_ok=True)
# logging configuration
logger = logging.getLogger('model_building')
logger.setLevel('DEBUG')

console_handler = logging.StreamHandler()
console_handler.setLevel('DEBUG')

log_file_path = os.path.join(log_dir, 'model_building.log')
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

def spliting_data(df):
   try:
    from sklearn.model_selection import train_test_split
    x = df.drop(columns=['Has_Asthma'])
    y = df['Has_Asthma']
    x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2,random_state=42)
    logger.debug('spliting of data completed !')
    return x_train, x_test, y_train, y_test
   except ValueError as v:
        logger.error('ValueError occurred: %s', v)
        raise
   except Exception as e:
        logger.error('Unexpected error occurred: %s', e)
        raise

def model_building(x_train, y_train):
   try:
      from sklearn.ensemble import RandomForestClassifier
      model = RandomForestClassifier()
      model.fit(x_train, y_train)
      logger.debug('model_building complete')
      return model
   except ValueError as v:
        logger.error('ValueError occurred: %s', v)
        raise
   except Exception as e:
        logger.error('Unexpected error occurred: %s', e)
        raise  
   
def save_model(model, file_path: str):
    """
    Save the trained model to a file.
    
    :param model: Trained model object
    :param file_path: Path to save the model file
    """
    try:
        # Ensure the directory exists
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        
        with open(file_path, 'wb') as file:
            pickle.dump(model, file)
        logger.debug('Model saved to %s', file_path)
    except FileNotFoundError as e:
        logger.error('File path not found: %s', e)
        raise
    except Exception as e:
        logger.error('Error occurred while saving the model: %s', e)
        raise   

def main():
    df = load_data(r'C:\Users\wadood\Desktop\my personal proj\Data\preprocesed_data.csv')    
    x_train, x_test, y_train, y_test = spliting_data(df)
    model =  model_building(x_train=x_train, y_train=y_train)
    save_model(model=model, file_path=r"C:\Users\wadood\Desktop\my personal proj\model\rf_model.pkl")

main()