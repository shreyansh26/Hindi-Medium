# Hindi Medium?

Microsoft Code.Fun.Do project.

The webapp is deployed [here](https://hindi-medium.herokuapp.com/).   
[Demo Video](https://youtu.be/c7Ub7QXtQVs)

This webapp takes a Video URL and generates subtitle files in English and Hindi, for it. The basic working of the webapp can be understood by the following steps - 

1. Scrape the video from the URL and convert it into an audio file.
2. Split the audio file into smaller files of length 5 seconds.
3. Use the audio files as input to the Microsoft Cognitive Services' Bing Speech API to convert it into text.
4. Use the generated text with Microsoft Cognitive Services' Translator Text API to convert the text into Hindi. (More languages can also be added, but we chose to go with Hindi)
5. Write the generated texts into a file with proper timestamps to make an "srt" file.

After these steps, the subtitles zip file is downloaded and a mail is sent to the user with the subtitle files attached.

## Limitations

Since, the webapp is currently deployed on Heroku, and Heroku times out the HTTP transactions after 30 seconds (and we require more time to generate the srt files for longer videos), our webapp is not able to support videos more than 40-50 seconds length.

So, for testing the app, please use a short video. Like [this](https://www.youtube.com/watch?v=jlmyJLnIOYw) one. On localhost, however, you can use a video as long as you wish.

## Testing

* Get API keys for Microsoft Cognitive Services' Bing Speech API and Translator Text API.
* If you wish to run just the scripts, make a file `config.py` in the `Scripts` directory, and add the constants `BING_SPEECH_API_KEY` and `TRANSLATE_TEXT_API_KEY`.
* To run the webapp, head to either the `Webapp/hindi` directory or the `Webapp-Heroku/hindi` directory.
* Enter the API keys in the files `audio2text.py` and `translatetext.py`.
* Also update `Webapp/hindi_medium/settings.py` or `Webapp-Heroku/hindi_medium/settings.py` with the proper Email host user and password you will be using for sending emails.
* Finally in either `Webapp` or `Webapp-Heroku` directory, run -    
  ```
  python3 manage.py migrate
  python3 manage.py runserver
  ```
* Head to [localhost](http://localhost:8000)

## Team Memebers

1. [Shreyansh Singh](https://github.com/shreyansh26)
2. [Shorya Jain](https://github.com/SJ255)
3. [Shrey Tanna](https://github.com/Shrey97)
