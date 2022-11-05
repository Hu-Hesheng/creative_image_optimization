from numba import jit, cuda

from imageai.Detection import ObjectDetection
import os
import sys
import warnings
import pandas as pd
from utils import *
warnings.filterwarnings('ignore')

# constants

IMAGES_EXT = ["JPG","PNG","GIF","WEBP","TIFF","PSD","RAW","BMP","HEIF","INDD","JPEG"]

VIDEO_EXT = ["WEBM","MPG","MP2","MPEG","MPE","MPV","OGG","MP4","M4P","M4V","AVI","WMV","MOV","QT","FLV","SWF"]

detector = ObjectDetection()
execution_path = os.getcwd()
# if model_path == None:
#     model_path = "../junk/data/resnet50_coco_best_v2.1.0.h5"
model_path = "../junk/data/resnet50_coco_best_v2.1.0.h5"

detector.setModelTypeAsRetinaNet()
detector.setModelPath( os.path.join(execution_path , model_path))
detector.loadModel()

def get_model(img_path):
    detections = detector.detectObjectsFromImage(input_image=os.path.join(execution_path , img_path), output_image_path=os.path.join(execution_path , model_path+"newI.jpg"))
    return detections

@jit(target_backend='cuda') 
def get_objects(img_path:str,model_path:str = None,print_objects:bool = False):
    
    detections = get_model(img_path)
    objects = []

    for eachObject in detections:
        objects.append(eachObject["name"])
        if print_objects:
            print(eachObject["name"] , " : " , eachObject["percentage_probability"] )
    return objects

# @jit(target_backend='cuda') 
def get_unique_objects(all_objects:list):
    unique_objects = list(set(all_objects))
    unique_objects_count = len(unique_objects)
    all_objects_count = len(all_objects)
    
    return all_objects,all_objects_count,unique_objects_count

# all in one
# @jit(target_backend='cuda') 
def add_object_feature(game_id:str):
    path  = f'/home/amanuel_zewdu/creative_image_optimization/data/Challenge_Data/Assets/{game_id}/'
    exclude = ["text","video","background"]
    file_names = get_files_name_with_extension_filter(path,IMAGES_EXT,exclude)
    all_objects = []
    for file_name in file_names:
        all_text = get_objects(path+file_name)
        all_objects.extend(all_text)
    return get_unique_objects(all_objects)