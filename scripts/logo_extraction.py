#!/home/natnael_masresha/.imageai/bin/python

from pytesseract import pytesseract
import cv2
from typing import List, Tuple
import matplotlib.pyplot as plt
import glob

pytesseract.tesseract_cmd = r'/usr/bin/tesseract'

import warnings
warnings.simplefilter("ignore")

DIRECTORY_PATH = "/home/amanuel_zewdu/creative_image_optimization/data/Challenge_Data/Assets/"

IMAGES_EXT = ["JPG","PNG","GIF","WEBP","TIFF","PSD","RAW","BMP","HEIF","INDD","JPEG"]

VIDEO_EXT = ["WEBM","MPG","MP2","MPEG","MPE","MPV","OGG","MP4","M4P","M4V","AVI","WMV","MOV","QT","FLV","SWF"]

def locate_image_on_image(locate_image: str, on_image: str, prefix: str = '', visualize: bool = False, color: Tuple[int, int, int] = (0, 0, 255)):
    try:

        image = cv2.imread(on_image)
        gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        shape = gray.shape

        
        template = cv2.imread(locate_image, 0)

        result = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF)
        _, _, _, max_loc = cv2.minMaxLoc(result)

        height, width = template.shape[:2]

        top_left = max_loc
        bottom_right = (top_left[0] + width, top_left[1] + height)

        if visualize:
            cv2.rectangle(image, top_left, bottom_right, color, 1)
            plt.figure(figsize=(10, 10))
            plt.axis('off')
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            plt.imshow(image)
        
        return (shape,top_left,bottom_right)
            
        
        # return {f'{prefix}top_left_pos': top_left, f'{prefix}bottom_right_pos': bottom_right}

    except cv2.error as err:
        # print(err)
        # top_left = (0,0)
        # bottom_right = (0,0)
        # shape = (0,0)

        # return (shape,top_left,bottom_right)
        raise Exception
    
def find_logo_position(folder_id:str,candidate_logo:list,ntry=0):
    
    prospect_on_image_names = ["preview","endframe","game"]
    max_try = len(prospect_on_image_names)

    try:

        img_path = glob.glob(f'{DIRECTORY_PATH}{folder_id}/*{prospect_on_image_names[ntry]}*.*')[0]
        logo_img = f'{DIRECTORY_PATH}{folder_id}/{candidate_logo[0]}'

        shape, top_left, bottom_right = locate_image_on_image(locate_image=logo_img, on_image=img_path)
        return (shape, top_left, bottom_right)
    
    except Exception as e:
        n = ntry + 1
        if n < max_try:
            return find_logo_position(folder_id,candidate_logo,n)
        return ((0,0), (0,0), (0,0))
    
def find_logo_area_ratio(shape:tuple,top_left:tuple,bottom_right:tuple):
    try:
        total_area = shape[0] * shape[1]
        logo_area = (bottom_right[0]-top_left[0]) * (bottom_right[1]-top_left[1])
        return logo_area/total_area
    except:
        return 0
