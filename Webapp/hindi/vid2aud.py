from __future__ import unicode_literals
import youtube_dl
import glob, os

def vid2aud(link, user):
	ydl_opts = {
	    'format': 'bestaudio/best',
	    'postprocessors': [{
	        'key': 'FFmpegExtractAudio',
	        'preferredcodec': 'wav',
	        'preferredquality': '192',
	    }],
	}
	with youtube_dl.YoutubeDL(ydl_opts) as ydl:
	    ydl.download([link])

	for file in glob.glob("./*.wav"):
	    os.rename(file, 'audio_'+str(user)+'.wav')
	#https://www.youtube.com/watch?v=JvOT4strzrA
