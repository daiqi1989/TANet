import cv2
import numpy as np



list_file = "/home/qid/blob/hd_vila/ffmpeg/sample.list"


with open(list_file,'r') as f:
    for line in f:
        namelist = line.split('\t')
        namelist[1] = namelist[1].strip()
        print(namelist[0])
        print(namelist[1])
        vd = cv2.VideoCapture(namelist[0])
        # vd.set(cv2.CAP_PROP_POS_FRAMES, 100)
        success, frame = vd.read()
        if success :
            cv2.imwrite(namelist[1],frame)
            print("write image")
        else:
            print("fail read frame")
