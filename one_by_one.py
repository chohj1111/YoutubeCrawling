from moviepy.editor import *
from pytube import Playlist, YouTube


url = "https://www.youtube.com/watch?v=fuS3cyc2U1M"
file_name = "Bubble_Sounds_UnderwaterDeep_Sleeping__Meditation__Spa__Calm_instantly44"
label = 'underwater_bubbling'
start_time = 0


yt = YouTube(url)
vids = yt.streams.all()
print(yt.title)
yt.streams.filter(adaptive=True, file_extension='mp4', only_video=True).order_by('resolution').desc().first().download('src/video/', file_name+ '.mp4')
yt.streams.filter(adaptive=True, file_extension='mp4', only_audio=True).order_by('abr').desc().first().download('src/audio/', file_name+ '.mp4')

videoclip = VideoFileClip("src/video/" + file_name+ '.mp4')
audioclip = AudioFileClip("src/audio/" + file_name+ '.mp4')
videoclip.audio = audioclip


#그 위에 영상을 합쳐서 파일이름으로 저장한다.
videoclip.write_videofile(file_name+ '.mp4')



# Slicing
for index in range(10):
  video = VideoFileClip(file_name+ '.mp4').subclip(start_time + index * 60, (start_time+10) + index * 60)
  video.write_videofile(label+'/'+file_name+'_'+ str(index)+ '.mp4')
