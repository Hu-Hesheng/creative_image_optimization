from load_data import Loader
from utils import *
from logo_extraction import *

class ExtractionPipeline():
    def __init__(self):
        
        self.DIRECTORY_PATH = "/home/amanuel_zewdu/creative_image_optimization/data/Challenge_Data/Assets/"
        self.IMAGES_EXT = ["JPG","PNG","GIF","WEBP","TIFF","PSD","RAW","BMP","HEIF","INDD","JPEG"]
        self.VIDEO_EXT = ["WEBM","MPG","MP2","MPEG","MPE","MPV","OGG","MP4","M4P","M4V","AVI","WMV","MOV","QT","FLV","SWF"]
        self.loader = Loader()