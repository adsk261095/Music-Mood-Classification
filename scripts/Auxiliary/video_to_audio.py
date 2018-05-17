# below is used to download ffmpeg if moviepy is giving issue
# import imageio
# imageio.plugins.ffmpeg.download()


import os
import moviepy.editor as mp
path='./dataset_videos_1'
for i in os.listdir(path):
	name=i[:i.find('.')]
	clip = mp.VideoFileClip("./dataset_videos_1/"+i)
	clip.audio.write_audiofile("./dataset_songs/"+name+".mp3")

	