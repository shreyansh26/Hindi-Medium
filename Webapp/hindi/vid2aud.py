from __future__ import unicode_literals
import youtube_dl
import glob, os

def vid2aud(link, user):
	if not os.path.exists(str(user)):
		os.mkdir(str(user))
	ydl_opts = {
	    'format': 'bestaudio/best',
	    'postprocessors': [{
	        'key': 'FFmpegExtractAudio',
	        'preferredcodec': 'wav',
	        'preferredquality': '192',
	    }],
	    'outtmpl': str(user)+'/%(title)s.%(ext)s'
	}

	for file in glob.glob('../'+str(user)+"/"+"*.wav"):
	    os.rename(file, 'audio_'+str(user)+'.wav')
	with youtube_dl.YoutubeDL(ydl_opts) as ydl:
	    ydl.download([link])
	#https://www.youtube.com/watch?v=JvOT4strzrA
