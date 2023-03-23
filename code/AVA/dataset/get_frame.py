from joblib import Parallel, delayed
import jsonlines
import json
from tqdm import tqdm
import time
import os
import math



metafile = "C:\\Users\\qid\\Downloads\\hdvila\\hdvila_part0.jsonl"


vs = []
with open(metafile,'r') as f:
    for l in jsonlines.Reader(f):
        # math.floor(len(l['clip'])/2)
        # print('/mnt/video/hd_vila_100m/video_clips_3fps/'+l['video_id']+'/'+l['clip'][math.floor(len(l['clip'])/2)]['clip_id'])
        cmd = "./ffmpeg -ss 00:00:04 -i " + '/home/qid/blob/hd_vila/hd_vila_100m/video_clips_3fps/'+l['video_id']+'/'+l['clip'][math.floor(len(l['clip'])/2)]['clip_id'] + " -frames:v 1 " + '\"/home/qid/blob/hd_vila/hd_vila_sample/'+l['video_id']+'.jpg\" #anything'
        vs.append(cmd)




with open('C:\\Users\\qid\\Downloads\\hdvila\\sample_hd.sh','w') as fid:
    for i in range(10000):
        fid.write(vs[i]+" \n")

print(len(vs))
