import nltk
from nltk.stem.snowball import SnowballStemmer

class NLP:
    allowed = ["Чизбургер", "Бургер", "Чай", "Вода", "Твистер", "КартошкаФри", "Картошка", "Кола", "Кокакола", "Гамбургер", "Чипсы", "Пирожок", "Пончик", "Пепси", "Баскет"]
    yes = ["да", "ага", "обычно", "дефолт", "всегда", "наверно"]
    no = ["нет", "неа", "новенькое", "не", "интересное", "необычное", "нестандартное"]

    def __init__(self):
        """
        Предобработка примеров и инициализаци инструментов для работы класса.
        """
        self.stemmer = SnowballStemmer("russian")
        self.yes_nlp_optimized = [self.stemmer.stem(i) for i in self.yes]
        self.no_nlp_optimized = [self.stemmer.stem(i) for i in self.no]
        self.products = []
        for product in self.allowed:
            self.products.append([self.stemmer.stem(product.lower()), product])
        print("NLP core has started")

    def get_yes_or_no(self, text):
        """
        Класифицирует текст как положительный или отрицательный ответ.
        Положительный - True
        Отрицательный - False
        """
        tokens = nltk.word_tokenize(text.lower())
        for i in tokens:
            i = self.stemmer.stem(i)
            if i in self.yes_nlp_optimized:
                return True
            if i in self.no_nlp_optimized:
                return False
        return False

    def get_dishes(self, text):
        """
        Выделяет из текста блюда, возвращает их список.
        """
        tokens = nltk.word_tokenize(text.lower())
        tags = nltk.pos_tag(tokens)
        res = []
        for (word, pos) in tags:
            if pos[:2] == 'NN':
                for product in self.products:
                    if self.stemmer.stem(word) == product[0]:
                        res.append(product[1])
        return res
