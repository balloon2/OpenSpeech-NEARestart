import os
import string
import pyttsx3
import speech_recognition as SR

class ProcessTranscripts():
    def __init__(self):
        #defining the stop words
        self.stpwrd=["um","ah","uh","er","huh"]
    def cleaned_text(self,rawTranscript):
        #format using string handling ops
        text=rawTranscript.lower
        wrds=text.split()
        cleaned=[]
        for i in wrds:
            if i not in self.stpwrd:
                cleaned.append(i)
        return cleaned
    def extractWrds(self,cleanedTxt):
        return cleanedTxt.split()
    
    class InitialTranscription():
        def __init__(self,micName):
            self.engine=pyttsx3.init()
            self.recogniser=SR.Recognizer()
            index=self.find_mic(micName)
            device_index=index
            self.mic=SR.Microphone(device_index)
        def speak(self,text):
            #speach to text
            self.engine.say(text)
            self.engine.runAndWait()
        def listen(self):
            with self.mic as source:
                print("speak")
                text=self.recogniser.listen(source)
                print("Time")
