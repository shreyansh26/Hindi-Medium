from bs4 import BeautifulSoup
import requests

class Microsoft_TTR():
    def __init__(self):
        self.sub_key = 'a4cc74a21ff74904b56f4600ce31ccf9'
        self.token = None
        pass

    def get_speech_token(self):
        cognitiveServiceUrl = 'https://api.cognitive.microsoft.com/sts/v1.0/issueToken'
        # Request Access Token
        requestHeader = {'Ocp-Apim-Subscription-Key': self.sub_key}
        responseResult = requests.post(cognitiveServiceUrl, headers=requestHeader)
        self.token = responseResult.text
        return True

    def translate(self, text):
        # Grab the token if we need it
        if self.token is None:
            print ("No Token... Getting one")
            self.get_speech_token()

        # Specify source and target language
        srcLanguage = "en"
        targetLanguage = "hi"
        #Specify URLs for Cognitive Services - Translator Text API
        translateUrl = 'https://api.microsofttranslator.com/v2/http.svc/Translate'
        # Define Parameters
        params = {'appid': 'Bearer '+ self.token, 'text': text, 'from': srcLanguage, 'to': targetLanguage}

        requestHeader = {'Accept': 'application/xml'}

        # Invoke Cognitive Services to perform translation
        responseResult = requests.get(translateUrl, params=params, headers=requestHeader)

        soup = BeautifulSoup(responseResult.text,"lxml")
        return  soup.get_text()
'''
if __name__ == "__main__":
    ms_ttr = Microsoft_TTR()
    ms_ttr.get_speech_token()
    text = "I am a boy."
    print("Text: ", text)
    print("Translated Text: ", ms_ttr.translate(text))'''