from videoprops import get_video_properties
import os
from os.path import exists
import shutil
import whratio

path = "C:/Users/RUDRA/Desktop/instagram/post/"
files = os.listdir(path)
story = "C:/Users/RUDRA/Desktop/instagram/story"
reels = "C:/Users/RUDRA/Desktop/instagram/reels"


def aspect():
    for filename in os.listdir(path):
        name, ext = os.path.splitext(filename)
        if ext == ".mp4":
            props = get_video_properties(path + filename)
            durationSTR = props["duration"]
            w = props["width"]
            h = props["height"]
            print(filename)
            a = whratio.as_float(w, h)
            duration = float(durationSTR)
            if not a >= 0.8 or duration > 61:
                if duration < 11:
                    shutil.move(os.path.join(path, filename), story)
                elif duration < 31:
                    shutil.move(os.path.join(path, filename), reels)


aspect()
# Recommended resolution is 1080 x 1920. 2,073,600
# Minimum resolution is 600 x 1067. 640,200