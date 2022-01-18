import csv
import os
import re

from pytube import YouTube


def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)


label = ""
with open('stylevideo_dataset_volcano.csv', 'r', encoding='utf-8') as f:
    rdr = csv.reader(f)
    next(rdr) # skip header

    for line in rdr:
        label = line[1]
        url = line[2]
        start_time = line[3]

        createFolder(label) # 폴더 만들기

        '''
            파일이름 공백제거
        '''
        yt = YouTube(url)   # youtube title로 file 이름 생성
        file_name = yt.title
        file_name = re.sub('[^a-zA-Z0-9 \n\.]', '', file_name)
        file_name = file_name.replace(" ", "_")
        file_name = label+"/"+file_name
        print(file_name)

        # start time
        for index in range(10):
          if os.path.isfile(file_name+'_'+ str(index) + '.mp4'):
            continue
          command = 'ffmpeg $(youtube-dl -g \''+ url +'\' | sed "s/.*/-ss '+ str(int(start_time) + index * 60) + ' -i &/") -loglevel error -t 10 -c copy -strict -2 ' + file_name+'_'+ str(index) + '.mp4'
          print(command)
          result = os.popen(command).read()
          #print(result)
          
result = os.popen("ls " + label + "/ -l | grep ^- | wc -l").read()
print(result)