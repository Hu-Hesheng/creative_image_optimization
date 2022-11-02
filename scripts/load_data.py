import pandas as pd
import zipfile
from io import StringIO
import smart_open as so
import boto3

class Loader():
    def __init__():
        pass
    def load_csv(bucket_path:str,file_path:str,save=False):
        with so.open(bucket_path, 'rb') as file_data:
            with zipfile.ZipFile(file_data) as z:
                with z.open(file_path) as zip_file_data:
                    csv_data = zip_file_data.read().decode("utf-8")
        
        csvStringIO = StringIO(csv_data)
        df = pd.read_csv(csvStringIO, sep=",", header=None)
        df.columns = df.iloc[0,:]
        df.drop(index=[0],inplace=True)

        if save:
            df.to_csv("../data/extracted.csv",index=False)

        return df
