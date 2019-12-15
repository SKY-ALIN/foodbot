from base import Base, engine, Session
from models import People, Dishes
Base.metadata.create_all(engine)

from TTS import TTS
from STT import STT
from NLP import NLP

import requests

def remember_dishes(session, person, dishes):
    """
    Функция перезаписи блюд клиента.
    """
    for dish in person.dishes:
        # Удаляем старые блюда
        session.delete(dish)
        session.commit()
    for dish in dishes:
        # ЗАпоминаем новые
        new_dish = Dishes(dish)
        new_dish.person = person
        session.add(new_dish)
        session.commit()

def send_to_kitchen(person, dishes):
    """
    Отправляем данные на кухню.
    """
    r = requests.post('http://194.67.220.170/dashboard/write_kitchen_data/', json={"client": person.name, "dishes": dishes})
    print("Status code:", r.status_code)

def main():
    TTSE = TTS()
    STTE = STT()
    NLPC = NLP()
    while True:
        if 1: # Если мы увидели покупателя
            if 1: # Мы знаем этого человека
                person_id = 1 # id распознанного человека из базы
                session = Session()
                person = session.query(People).filter(People.id == person_id).first()
                TTSE.say("Добрый день {}".format(person.name))

                TTSE.say("Вам как обычно или чего-нибудь новенького?")
                answer = STTE.recognize()
                if answer:
                    # Узнаём положительный ли или отрицательный клиент дал ответ
                    if NLPC.get_yes_or_no(answer):
                        send_to_kitchen(person, person.dishes)
                        dishes = ""
                        for dish in person.dishes:
                            dishes += " " + dish
                        TTSE.say("Хорошо, сейчас сделаем как обычно"+temp)
                        TTSE.say("Приятного время провождения, {}!".format(person.name))
                    else:
                        dishes = NLPC.get_dishes(answer)
                        # Проверяем содержался ли ответ в первом ответе клиента
                        # (А такое вполне возможно)
                        if dishes:
                            send_to_kitchen(person, dishes)
                            temp = ""
                            for dish in dishes:
                                temp += " " + dish
                            TTSE.say("Заказ"+temp+" принят!")
                            remember_dishes(session, person, dishes)
                            TTSE.say("Приятного время провождения, {}!".format(person.name))
                        else:
                            TTSE.say("Хорошо, {}, чего бы вы тогда хотели заказать?".format(person.name))
                            answer = STTE.recognize()
                            if answer:
                                dishes = NLPC.get_dishes(answer)
                                if dishes:
                                    send_to_kitchen(person, dishes)
                                    temp = ""
                                    for dish in dishes:
                                        temp += " " + dish
                                    TTSE.say("Заказ"+temp+" принят!")
                                    remember_dishes(session, person, dishes)
                                    TTSE.say("Приятного время провождения, {}!".format(person.name))
                                else:
                                    TTSE.say("Я так и не услышала названия блюд.")
                            else:
                                TTSE.say("Не могу распознать.")
                else:
                    TTSE.say("Не могу распознать.")
                session.close()
                exit()
            else: # Если мы его не знаем
                TTSE.say("Что вы хотели бы заказать?")
                answer = STTE.recognize()
                if answer:
                    dishes = NLPC.get_dishes(answer)
                    if dishes:
                        send_to_kitchen("Неизвестный клиент", dishes)
                        temp = ""
                        for dish in dishes:
                            temp += " " + dish
                        TTSE.say("Заказ"+temp+" принят!")
                        TTSE.say("Приятного время провождения!")
                    else:
                        TTSE.say("Я так и не услышала названия блюд.")
                else:
                    TTSE.say("Не могу распознать.")

if __name__ == '__main__':
	main()
