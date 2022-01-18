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




'''
    파일이름 공백제거
'''
url = "https://www.youtube.com/watch?v=3aezPSwUf4s"
yt = YouTube(url)   # youtube title로 file 이름 생성

label = "thunder"
file_name = yt.title
file_name = re.sub('[^a-zA-Z0-9 \n\.]', '', file_name)
file_name = file_name.replace(" ", "_")
file_name = label+"/"+file_name

# start time
start_time = 2
for index in range(10):
    if os.path.isfile(file_name+'_'+ str(index) + '.mp4'):
        continue
    command = 'ffmpeg $(youtube-dl -g \''+ url +'\' | sed "s/.*/-ss '+ str(int(start_time) + index * 60) + ' -i &/") -t 10 -c copy -strict -2 ' + file_name+'_'+ str(index) + '.mp4'
    result = os.popen(command).read()
    print(result)
