import numpy as np
import pandas as pd
import cv2
import os

from random import shuffle

""" WHAT'S THE FORMAT I WANT? METADATA (accident/no_accident)  SEPARATELY, PATHS TO IMAGES ELSEWHERE """


# Get the frames, videos, ... for the videos with accidents
acc_paths = []
acc_times = []

duos = []
i = 0 # Current output video
frame_opath = "/home/dd/arcelormittalvideos/accident_frames/final/"
with open("accident_times.txt", "r") as f:
    for line in f.readlines():
        vid, duration = line.strip().split(" ")

        # ENH: Also detect 1 class and 0 class types
        if duration in ["-1","many", "none", "0:00", "None"]: print("Skipping{}".format(vid));continue
        duos.append((vid, duration))

    # OK, we got the duos. Now shuffle and iterate again
    shuffle(duos)
    print("We have {} videos".format(len(duos)))
    for vid_idx, (vid, duration) in enumerate(duos):

        ipath = "/home/dd/arcelormittalvideos/accident{}".format(vid)
        if not os.path.exists(ipath): print("{} not existing".format(ipath))
        cap = cv2.VideoCapture(ipath)
        video_length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) - 1
        def getFrame(sec, i, vid, cls):
            cap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
            hasFrames,image = cap.read()
            if hasFrames:
                print("Writing")
                this_o_path = frame_opath
                if vid_idx < len(duos) * 0.8:
                    subdir = "train"
                else:
                    subdir = "val"
                this_o_path = this_o_path + os.sep + subdir
                if not os.path.exists(this_o_path): os.mkdir(this_o_path)
                # Also add class
                this_o_path = this_o_path + os.sep + str(cls)
                if not os.path.exists(this_o_path): os.mkdir(this_o_path)
                
                cv2.imwrite(this_o_path + os.sep + vid +"_"+str(i)+"_"+str(cls)+".jpg", image)     # save frame as JPG file
            return hasFrames

        sec = 0
        frameRate = 1
                
        minutes, seconds = duration.split(":")
        total_seconds = int(minutes) * 60 + int(seconds)
        print(total_seconds)
    
        # Get before the accident
        success = True
        while success and sec < total_seconds:
            sec = sec + frameRate
            sec = round(sec, 2)
            i = i + 1
            success = getFrame(sec, i, vid, 0)
        
        # Get after the accident
        while success and sec < 2 * total_seconds:
            sec = sec + frameRate
            sec = round(sec, 2)
            i = i + 1
            success = getFrame(sec, i, vid, 1)
            
        cap.release()


