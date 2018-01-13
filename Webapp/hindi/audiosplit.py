from pydub import AudioSegment
import os
import wave
import contextlib
from math import ceil

def audiosplit(user):
	fname = str(user)+'/audio_'+str(user)+'.wav'
	if not os.path.exists('./Splits_' +str(user)):
		os.mkdir('Splits_' +str(user))

	with contextlib.closing(wave.open(fname,'r')) as f:
	    frames = f.getnframes()
	    rate = f.getframerate()
	    duration = frames / float(rate)
	    duration *= 1000
	    duration = int(ceil(duration))
	    print(duration)

	t1 = 0 #Works in milliseconds
	t2 = 5000
	newAudio = AudioSegment.from_wav('audio_'+str(user)+'.wav')
	i = 1
	while(1):
		if(t1>duration):
			break
		newAudio2 = newAudio[t1:t2]
		newAudio2.export('./Splits_' +str(user)+'/'+str(i)+'.wav', format="wav")
		t1 += 5000
		t2 += 5000
		i+=1
