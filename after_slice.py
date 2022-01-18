from moviepy.editor import *

label = 'volcano'
file_name = ""
start_time = 

# 시작시간 수정
for index in range(10):
  video = VideoFileClip(file_name + '.mp4').subclip(start_time + index * 60, (start_time+10) + index * 60)
  video.write_videofile(label + '/' + file_name+'_'+ str(index)+ '.mp4')