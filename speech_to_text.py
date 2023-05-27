import os

import playsound
import speech_recognition as sr
from gtts import gTTS

r = sr.Recognizer() 
def speak(text):
    tts = gTTS(text=text, lang="vi")
    filename="voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)

while True:
    robot_brain = ""
    with sr.Microphone() as source:
        audio_data=r.record(source, duration=5)
        try:
            text=r.recognize_google(audio_data, language="vi")
        except:
            text=""
        print(text)
        speak(text)
          
        
        
