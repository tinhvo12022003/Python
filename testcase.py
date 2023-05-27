import speech_recognition as sr
from gtts import gTTS
import os
import time
import playsound
from datetime import datetime 
from datetime import date
import calendar
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

        if(text == ""):
            print("Không nghe rõ")
        elif "thoát" and "hệ" and "thống" in text:
            print("Đang rời hệ thống")
            break
        elif "xin" and "chào"in text:
            print("Xin chào")
        elif "Bạn" and "là" and "ai" in text:
            print("Tôi là trợ lý ảo")
        
        elif "Viết bằng" and "ngôn ngữ" and "nào" in text:
            print("Tôi được thiết kê bằng python")
        # elif "ngày" and "mấy" in text:
        #     print("hôm nay là " + str(date.today()))
        elif "mấy" and "giờ" in text:
            print("Bây giờ là:" + str(datetime.now().hour) +" giờ " + str(datetime.now().minute)+" phút " + str(datetime.now().second) + "giây")    
        elif "lịch" and "hiện tại" in text:
            cal = calendar.month(date.today().year, date.today().month)
            print(cal)
        elif "Hôm nay" and "thứ mấy" in text:\
            print("hôm nay là " + str(date.today()))
        else:
            print("Không có dữ liệu")
        
        
            
        