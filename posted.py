import os
from os.path import exists
from shutil import move, Error
import string
import random

target_dir = "C:/Users/RUDRA/Desktop/instagram/posted/"
src_dir = "C:/Users/RUDRA/Desktop/instagram/post/"


def posted(file_name):

    try:
        move(os.path.join(src_dir, file_name), os.path.join(target_dir, file_name))
    except Error as e:
        print("+++++++++++++++++++++++++++++++++++")
        print(e)
        print("++++++++++++++++++++++++++++++++++++")
