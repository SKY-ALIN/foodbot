import nltk

yes_or_no_texts = ["Мне как обычно", "Давай как всегда", "Да, по дефолту", "Не, хочу чего-нибудь новенького", "Новеное", "Нет, давай новое"]
diches_texts = ["Дайте мне колу с бургером", "Я хотел бы чизбургер с твистером", "Робот, дай ка мне просто чаю"]

def get_yes_or_no(text):
    pass

def get_dishes(text):
    tokens = nltk.word_tokenize(text.lower())
    tags = nltk.pos_tag(tokens)
    # nouns = []
    # for (word, pos) in tags:
    #     if pos == 'NN':
    #         nouns.append(word)
    nouns = [word for (word, pos) in tags if pos == 'NN']
    return nouns
