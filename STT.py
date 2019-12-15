import speech_recognition as sr
from pygame import mixer
import time
import os

class STT:
    """
    Движок для распознавания речи. Работает как надстройка над сборкой из
    разных сервисов от google, amazon, microsoft и т.д.
    """
    def __init__(self):
        self.recognizer = sr.Recognizer()
        print("STT engine has started")

    def pip(self):
        """
        Подача звукогого сигнала.
        """
        mixer.init()
        f=open("pip.mp3","rb")
        mixer.music.load(f)
        mixer.music.play()
        while mixer.music.get_busy():
            time.sleep(0.1)
        mixer.stop()
        mixer.quit()
        f.close()

    def recognize(self):
        self.pip()
        os.system('arecord -D plughw:1,0 -d 5 clientVoice.wav')
        print("Listen microphone...")
        self.pip()
        with sr.AudioFile("clientVoice.wav") as source: # device_index=2
            audio = self.recognizer.record(source)

        # try:
        #     print("Recognizing speech via sphinx...")
        #     text = self.recognizer.recognize_sphinx(audio)
        #     print("Recognized text:", text)
        #     return text
        # except sr.UnknownValueError:
        #     print("Can't recognize via sphinx")
        # except sr.RequestError as e:
        #     print("Service error:", e)

        try:
            print("Recognizing speech via google...")
            text = self.recognizer.recognize_google(audio, language="ru-RU")
            print("Recognized text:", text)
            return text
        except sr.UnknownValueError:
            print("Can't recognize via google")
        except sr.RequestError as e:
            print("Service error:", e)

        return False
