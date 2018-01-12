import os
from audio2text import Microsoft_ASR
from translatetext import Microsoft_TTR
from vid2aud import vid2aud
from audiosplit import audiosplit

vid2aud()
audiosplit()
ms_asr = Microsoft_ASR()
ms_asr.get_speech_token()
ms_ttr = Microsoft_TTR()
ms_ttr.get_speech_token()
num_files = len(os.listdir('./Splits/'))
for i in range(1, num_files+1):
	text, confidence = ms_asr.transcribe('./Splits/'+str(i)+'.wav')
	print ("Text: ", text)
	print ("Confidence: ", confidence)
	if text==" ":
		translated_text = " "
	else:
		translated_text = ms_ttr.translate(text)
	print ("Translated Text: ", translated_text)