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

OFFSET = 10 # HOW FAR WE PREDICT IN THE FUTURE, HORIZON REALLY
WINDOW = 4 * OFFSET # HOW FAR BEFORE AND AFTER WE KEEP OBSERVATIONS FOR

frame_opath = "/home/dd/arcelormittalvideos/accident_frames/{}sfinal".format(OFFSET)
if WINDOW != -1:
    frame_opath = frame_opath + str(WINDOW)
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

        frameRate = 1
                
        minutes, seconds = duration.split(":")
        total_seconds = int(minutes) * 60 + int(seconds)
        print(total_seconds)

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
                this_cls = 0 if (sec + OFFSET)< total_seconds else 1
                this_o_path = this_o_path + os.sep + str(this_cls)
                if not os.path.exists(this_o_path): os.mkdir(this_o_path)

                # Maybe WINDOW is set: then we only keep around the event
                if WINDOW == -1 or (((total_seconds - OFFSET) <= sec ) and (sec <= total_seconds + OFFSET)):
                    cv2.imwrite(this_o_path + os.sep + vid +"_"+str(i)+"_"+str(this_cls)+".jpg", image)     # save frame as JPG file
            return hasFrames

        sec = 0
    
        # Get before the accident
        success = True
        while success and sec < total_seconds:
            sec = sec + frameRate
            sec = round(sec, 2)
            i = i + 1
            success = getFrame(sec, i, vid, 0)
        
        # Get after the accident
        while success and sec < 2 * total_seconds - OFFSET:
            sec = sec + frameRate
            sec = round(sec, 2)
            i = i + 1
            success = getFrame(sec, i, vid, 1)
            
        cap.release()


