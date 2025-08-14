import pandas as pd
from sklearn.model_selection import train_test_split
import os
import logging
import pickle

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
   
def load_model(file_path: str):
    """Load the trained model from a file."""
    try:
        with open(file_path, 'rb') as file:
            model = pickle.load(file)
        logger.debug('Model loaded from %s', file_path)
        return model
    except FileNotFoundError:
        logger.error('File not found: %s', file_path)
        raise
    except Exception as e:
        logger.error('Unexpected error occurred while loading the model: %s', e)
        raise

def save_prediction(x_test,model, desstination: str):
   try:
      Data = pd.read_csv(r'C:\Users\wadood\Desktop\my personal proj\main_data\synthetic_asthma_dataset.csv')
      prediction = model.predict(x_test)
      probs = model.predict_proba(x_test)[:, 1]

      ids_for_test = Data.loc[x_test.index, 'Patient_ID']
      output_df = pd.DataFrame({
    'id': ids_for_test,
    'prediction': prediction,
    'probability': probs
     })
      output_df.to_csv(desstination, index=False)
      logger.debug('prediction saved to destination successfully !!')
   except ValueError as v:
        logger.error('ValueError occurred: %s', v)
        raise
   except Exception as e:
        logger.error('Unexpected error occurred: %s', e)
        raise
   except FileNotFoundError:
        logger.error('File not found: %s', desstination)
        raise


def main():
    df = load_data(r'C:\Users\wadood\Desktop\my personal proj\Data\preprocesed_data.csv')
    x_train, x_test, y_train, y_test = spliting_data(df)
    model = load_model(r'C:\Users\wadood\Desktop\my personal proj\model\rf_model.pkl')
    save_prediction(x_test, model, desstination=r"C:\Users\wadood\Desktop\my personal proj\Final prediction of data\predictions.csv")

main()    