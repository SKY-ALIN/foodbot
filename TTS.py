import os
import re
import time
import datetime
from pygame import mixer
from gtts import gTTS

class TTS:
    """
    Движок для синтеза речи. Работает как надстройка над библиотекой gTTS
    использующей сервисы google.
    """
    def __init__(self):
        mixer.init()
        print("TTS engine has started")

    def say(self, what, l='ru'):
    	mixer.init()
    	print(datetime.datetime.today().strftime("%H:%M:%S -"), what)
    	tts=gTTS(text=what, lang=l)
    	mp3 = "speech.mp3"
    	tts.save(mp3)
    	f=open(mp3,"rb")
    	mixer.music.load(f)
    	mixer.music.play()
    	while mixer.music.get_busy():
    		time.sleep(0.1)
    	mixer.stop()
    	mixer.quit()
    	f.close()
    	os.remove(mp3)
