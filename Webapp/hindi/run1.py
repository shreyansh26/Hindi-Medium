import os
from .audio2text import Microsoft_ASR
from .translatetext import Microsoft_TTR
from .vid2aud import vid2aud
from .audiosplit import audiosplit
import shutil

def main(link):
	vid2aud(link)
	audiosplit()
	ms_asr = Microsoft_ASR()
	ms_asr.get_speech_token()
	ms_ttr = Microsoft_TTR()
	ms_ttr.get_speech_token()

	f_en = open("english_subtitles.srt", "w")
	f_hi = open("hindi_subtitles.srt", "w")

	num_files = len(os.listdir('./Splits/'))
	cnt = 0
	start = 0
	end = 5
	for i in range(1, num_files+1):
		flag = 0
		text, confidence = ms_asr.transcribe('./Splits/'+str(i)+'.wav')
		print ("Text: ", text)
		print ("Confidence: ", confidence)
		if text==" ":
			translated_text = " "
		else:
			translated_text = ms_ttr.translate(text)
			flag = 1
			cnt += 1
		print ("Translated Text: ", translated_text)
		if flag == 1:
			start_hours = start//3600
			temp = start%3600
			start_min = temp//60
			start_sec = temp%60
			end_hours = end//3600
			temp = end%3600
			end_min = temp//60
			end_sec = temp%60

			if(start_hours <= 9):
				start_hours = '0' + str(start_hours)
			else:
				start_hours = str(start_hours)
			if(start_min <= 9):
				start_min = '0' + str(start_min)
			else:
				start_min = str(start_min)
			if(start_sec <= 9):
				start_sec = '0' + str(start_sec)
			else:
				start_sec = str(start_sec)

			if(end_hours <= 9):
				end_hours = '0' + str(end_hours)
			else:
				end_hours = str(end_hours)
			if(end_min <= 9):
				end_min = '0' + str(end_min)
			else:
				end_min = str(end_min)
			if(end_sec <= 9):
				end_sec = '0' + str(end_sec)
			else:
				end_sec = str(end_sec)
			f_en.write(str(cnt)+"\n")
			f_en.write(start_hours+':'+start_min+':'+start_sec+',001 --> '+end_hours+':'+end_min+':'+end_sec+',000\n')
			f_en.write(text+'\n')
			f_en.write('\n')
			f_hi.write(str(cnt)+"\n")
			f_hi.write(start_hours+':'+start_min+':'+start_sec+',001 --> '+end_hours+':'+end_min+':'+end_sec+',000\n')
			f_hi.write(translated_text+'\n')
			f_hi.write('\n')
		start += 5
		end += 5

	f_en.close()
	f_hi.close()
	shutil.rmtree('./Splits')

if(__name__ == '__main__'):
	main()
