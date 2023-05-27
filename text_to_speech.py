import speech_recognition as sr
from gtts import gTTS
import os
import playsound

def speak(text):
    tts = gTTS(text=text, lang='vi')
    filename='voice.mp3'
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)

str = 'Tôi muốn tắt nắng đi Cho màu đừng nhạt mất; Tôi muốn buộc gió lại Cho hương đừng bay đi. Của ong bướm này đây tuần tháng mật; Này đây hoa của đồng nội xanh rì; Này đây lá của cành tơ phơ phất; Của yến anh này đây khúc tình si; Và này đây ánh sáng chớp hàng mi, Mỗi sáng sớm, thần Vui hằng gõ cửa; Tháng giêng ngon như một cặp môi gần; Tôi sung sướng. Nhưng vội vàng một nửa: Tôi không chờ nắng hạ mới hoài xuân.'
speak(str)