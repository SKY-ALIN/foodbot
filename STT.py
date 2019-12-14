import speech_recognition as sr
from pygame import mixer
import time

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
        with sr.Microphone(device_index=2) as source: # device_index=2
            print("Listen microphone")
            audio = self.recognizer.listen(source)
            self.pip()
        try:
            text = self.recognizer.recognize_google(audio, language="ru-RU")
            print("Recognized text:", text)
            return text
        except sr.UnknownValueError:
            print("Can't recognize")
        except sr.RequestError as e:
            print("Service error:", e)
        return False
