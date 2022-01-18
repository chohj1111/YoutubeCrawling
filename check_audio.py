import csv
import os
import re
from pytube import YouTube

with open('stylevideo_dataset_volcano.csv', 'r', encoding='utf-8') as f:
    rdr = csv.reader(f)
    next(rdr) # skip header
    label=""
    for line in rdr:
        label = line[1]
        file_path = line[4] 
        
        command = 'ffprobe -i '+ file_path+ '_0.mp4 -show_streams 2>&1 | grep \'Stream #0:1\''
        print(file_path)
        
        result = os.popen(command).read()
        if(len(result) == 0): 
          print ("****************Empty****************")
          print()
        else: 
          print  (result)

    result = os.popen("ls " + label + "/ -l | grep ^- | wc -l").read()
    print(result)          