import speech_recognition as sr
from pygame import mixer
import time

class STT:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        print("STT engine has started")

    def pip(self):
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
        with sr.Microphone() as source:
            print("Listen microphone")
            audio = self.recognizer.listen(source)
            self.pip()
        try:
            text = self.recognizer.recognize_google(audio, language="ru-RU")
            print("Recognized test:", text)
            return text
        except sr.UnknownValueError:
            print("Can't recognize")
        except sr.RequestError as e:
            print("Service error:", e)
        return False
