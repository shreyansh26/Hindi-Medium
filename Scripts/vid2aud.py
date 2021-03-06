from __future__ import unicode_literals
import youtube_dl
import glob, os

def vid2aud():
	ydl_opts = {
	    'format': 'bestaudio/best',
	    'postprocessors': [{
	        'key': 'FFmpegExtractAudio',
	        'preferredcodec': 'wav',
	        'preferredquality': '192',
	    }],
	}
	with youtube_dl.YoutubeDL(ydl_opts) as ydl:
	    ydl.download(['https://www.youtube.com/watch?v=jlmyJLnIOYw'])

	for file in glob.glob("./*.wav"):
	    os.rename(file, 'audio.wav')
	#https://www.youtube.com/watch?v=JvOT4strzrA