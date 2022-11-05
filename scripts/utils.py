import os
import sys

def get_files_name_with_extension_filter(directory:str, filter_extension:list=None,exclude_names:list=None)->list:
    
    # directory = f'/home/amanuel_zewdu/creative_image_optimization/data/Challenge_Data/Assets/{directory}/'
    
    files = []
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        
        # checking if it is a file
        if filter_extension != None:
            if os.path.isfile(f):
                if ~any(substring in filename.split('.')[0] for substring in exclude_names):
                    if filename.split('.')[-1].upper() in filter_extension:
                        files.append(filename)
        else:
            if os.path.isfile(f):
                if ~any(substring in filename.split('.')[0] for substring in exclude_names):
                    files.append(filename)

    return files

def get_files_name(directory:str, filter_extension:list=None)->list:
    
    # directory = f'/home/amanuel_zewdu/creative_image_optimization/data/Challenge_Data/Assets/{directory}/'
    
    files = []
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        
        # checking if it is a file
        if filter_extension != None:
            if os.path.isfile(f):
                if filename.split('.')[-1].upper() in filter_extension:
                    files.append(filename)
        else:
            if os.path.isfile(f):
                files.append(filename)

    return files

def get_unique_objects(all_objects:list):
    unique_objects = list(set(all_objects))
    unique_objects_count = len(unique_objects)
    all_objects_count = len(all_objects)
    
    return all_objects,all_objects_count,unique_objects_count

def filter_list(all_values:list,key_word:str):
    filtered_list = filter(lambda x: key_word in x.lower(), all_values)
    return list(filtered_list)