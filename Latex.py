"""
File: Latex.py
Author: Jackson Bates
Created: 6/2/2019 1:41 AM 
"""

if __name__ == '__main__':
    #import tensorflow as tf
    import logging
    import os
    import sys
    import itertools


    #print("TF Version: {}".format(tf.__version__))


    images_dir = os.getcwd()+"\\handwrittenmathsymbols\\data\\extracted_images"
    folders = os.listdir(images_dir)
    folders = {item:[] for item in folders}
    print("folders initialized: {}".format(folders))
    for item in folders.keys():
        print("Adding to '{}' folder list".format(item))
        for img_name in os.listdir(images_dir+"\\"+item):
            print("image: {}".format(img_name))
            folders[item].append(img_name)

    print(folders)


