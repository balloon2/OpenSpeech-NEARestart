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
        text=rawTranscript.lower()
        wrds=text.split()
        cleaned=[]
        for i in wrds:
            if i not in self.stpwrd:
                cleaned.append(i)
        return cleaned
    def extractWrds(self,cleanedTxt):
        return " ".join(cleanedTxt.split())
    
class InitialTranscription():
    def __init__(self,micName):
        self.engine=pyttsx3.init()
        self.recogniser=SR.Recognizer()
        index=self.find_mic(micName)
        device_index=index
        self.mic=SR.Microphone(device_index)
    def find_mic(self,micName):
        if not micName:
            pass
        names=SR.Microphone.list_microphone_names()
        for i in range(len(names)):
            if micName.lower() in names[i].lower():
                return i 

    def speak(self,text):
        #speach to text
        self.engine.say(text)
        self.engine.runAndWait()
    def listen(self):
        with self.mic as n:
            self.recogniser.adjust_for_ambient_noise(n)
            print("adjusted for ambient noise")
            print("speak")
            audio=self.recogniser.listen(n)
            print("Time")
        try:
            text=self.recogniser.recognize_whisper(audio, model="base",language="english")
        except SR.UnknownValueError:
            self.speak("sorry we couldnt quite catch that")
            print("sorry we couldnt quite cacth that")
        except SR.RequestError:
            print(SR.RequestError)
            self.speak("an error has occured")
        finally:
            print("an error has occured")
            self.speak("an error has occured")