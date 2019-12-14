import speech_recognition as sr

class STT:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def recognize(self):
        with sr.Microphone() as source:
            print("Listen microphone")
            audio = self.recognizer.listen(source)
        try:
            text = r.recognize_google(audio, language="ru-RU")
            print("Recognized test:", text)
            return text
        except sr.UnknownValueError:
            print("Can't recognize")
        except sr.RequestError as e:
            print("Service error:", e)
        return False
