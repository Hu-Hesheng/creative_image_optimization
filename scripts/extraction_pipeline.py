import pandas as pd
from load_data import Loader
from utils import *
from logo_extraction import *
from object_extraction import *
from text_extraction import *

class ExtractionPipeline():
    def __init__(self,csv_path:str=None,directory_path:str=None,bucket:str = None,save_files:bool=False):
        
        if directory_path == None:
            directory_path = "/home/amanuel_zewdu/creative_image_optimization/data/Challenge_Data/Assets/"
               
        if bucket == None:
            bucket = "s3://10ac-batch-6/data/w11/Challenge_Data.zip"
            
        if csv_path == None:
            csv_path = "Challenge_Data/performance_data.csv"
            
        self.IMAGES_EXT = ["JPG","PNG","GIF","WEBP","TIFF","PSD","RAW","BMP","HEIF","INDD","JPEG"]
        self.VIDEO_EXT = ["WEBM","MPG","MP2","MPEG","MPE","MPV","OGG","MP4","M4P","M4V","AVI","WMV","MOV","QT","FLV","SWF"]
        
        self.loader = Loader()
        self.save_files = save_files
        self.directory_path = directory_path
        df = self.loader.load_csv(bucket,csv_path)
        self.df = df
        
    def extract_text(self,df:pd.DataFrame=None) -> pd.DataFrame:
        if df == None:
            df_text = self.df.copy()
        else:
            df_text = df.copy()
            
        df_text["all_text"] = df_text.game_id.apply(lambda x:add_text_feature(x))
        if self.save_files:
            df_text.to_csv("creatives_with_text.csv")
            
        return df_text
    
    def extract_objects(self,df:pd.DataFrame=None) -> pd.DataFrame:
        if df == None:
            df_object = self.df.copy()
        else:
            df_object = df.copy()
            
        df_object[['all_objects','all_objects_count','unique_objects_count']] = df_object.game_id.apply(lambda x:pd.Series(add_object_feature(x)))
        if self.save_files:
            df_object.to_csv("creatives_with_objects.csv")
            
        return df_object
    
    def extract_logo(self,df:pd.DataFrame=None) -> pd.DataFrame:
        if df == None:
            df_logo = self.df.copy()
        else:
            df_logo = df.copy()
        
        df_logo.drop(columns=["preview_link","ER","CTR"],inplace=True)
        df_logo["all_files"] = df_logo.game_id.apply(lambda x:get_files_name(f'{DIRECTORY_PATH}{x}/'))
        df_logo['concat'] = df_logo.all_files.apply(lambda x: " ".join(x))
        
        contain_logo = df_logo[df_logo.concat.str.lower().str.contains("logo")]
        contain_logo['file_name'] = contain_logo.all_files.apply(lambda x: filter_list(x,"logo"))
        contain_logo.drop(columns=["all_files","concat"],inplace=True)
        contain_logo[["shape","top_left","bottom_right"]] =  contain_logo.apply(lambda x: pd.Series(find_logo_position(x.game_id,x.file_name)) ,axis = 1)
        contain_logo[["LAR"]] =  contain_logo.apply(lambda x: pd.Series(find_logo_area_ratio(x["shape"],x["top_left"],x["bottom_right"])) ,axis = 1)
        contain_logo["LAR"] =  contain_logo.LAR.apply(lambda x: x if x <=1 else 0 )
        if self.save_files:
            contain_logo.to_csv("creatives_with_logo_information.csv")
        
        return contain_logo
