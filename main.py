from TTS import TTS
from STT import STT

def main():
    TTSE = TTS()
    STTE = STT()
    while True:
        if 1: # Если мы увидели покупателя
            if 1: # Мы знаем этого человека
                TTSE.say("Вам как обычно или чего-нибудь новенького?")
                answer = STTE.recognize()
                if answer:
                    print(answer)
                    TTSE.say("Принято.")
                else:
                    TTSE.say("Не могу распознать.")
                exit()
            else: # Если мы его не знаем
                TTSE.say("Что вы хотели бы заказать?")
        else:
            pass # Если мы никого не видим

if __name__ == '__main__':
	main()
