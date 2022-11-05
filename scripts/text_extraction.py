from pytesseract import pytesseract
import cv2
import numpy as np
from typing import List, Tuple
import matplotlib.pyplot as plt
from PIL import Image

import os
import sys 
from utils import *
pytesseract.tesseract_cmd = r'/usr/bin/tesseract'

# constants

IMAGES_EXT = ["JPG","PNG","GIF","WEBP","TIFF","PSD","RAW","BMP","HEIF","INDD","JPEG"]

VIDEO_EXT = ["WEBM","MPG","MP2","MPEG","MPE","MPV","OGG","MP4","M4P","M4V","AVI","WMV","MOV","QT","FLV","SWF"]

def get_pure_list(text:str):
    text_list = (text).split('\n')

    while ' ' in text_list:
        text_list.remove(' ')

    while '' in text_list:
        text_list.remove('')

    while '\x0c' in text_list:
        text_list.remove('\x0c')
        
    return text_list

def get_text(img_path:str,convert_to_gray:bool=True,plot:bool=False):
    
    img = cv2.imread(img_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    if plot:
        plt.subplot(1,2,1)
        plt.imshow(img)

        plt.subplot(1,2,2)
        plt.imshow(gray)

        plt.show()
    if convert_to_gray:
        return get_pure_list(pytesseract.image_to_string(gray))
    else:
        return get_pure_list(pytesseract.image_to_string(img))
    
    
def add_text_feature(game_id:str):
    path  = f'/home/amanuel_zewdu/creative_image_optimization/data/Challenge_Data/Assets/{game_id}/'
    file_names = get_files_name(path,IMAGES_EXT)
    all_texts = []
    for file_name in file_names:
        all_text = get_text(path+file_name)
        all_texts.extend(all_text)
    return all_texts

def add_engagement_type(all_text:list):
    joined_text = " ".join(all_text)
    joined_text = joined_text.lower()
    
    if ("swipe right" in joined_text) or ("swipe to the right" in joined_text):
        return "swipe right"
    elif ("swipe left" in joined_text) or ("swipe to the left" in joined_text):
        return "swipe left"
    elif "tap and hold" in joined_text:
        return "tap and hold"
    elif "scrub" in joined_text:
        return "scrub"
    elif "tap" in joined_text:
        return "tap"