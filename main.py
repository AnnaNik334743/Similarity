import urllib.request
import gensim
from gensim.models import word2vec
import re
import pymorphy2


def install_model():  # нужно прогнать один раз, чтобы загрузить модель
    urllib.request.urlretrieve("https://rusvectores.org/static/models/web_upos_cbow_300_20_2017.bin.gz",
                               "web_upos_cbow_300_20_2017.bin.gz")


def clean_form(word):  # убирает из слов всякую несуразицу и приводит их к начальной форме
    word = re.sub(r'[^a-zA-Zа-яА-Я-+]', '', word)
    morph = pymorphy2.MorphAnalyzer()
    p = morph.parse(word)[0]
    norm_form = p.normal_form
    new_word = norm_form + '_' + morph.parse(norm_form)[0].tag.POS
    new_word = re.sub(r'ADJF|ADJS', 'ADJ', re.sub(r'ADVB', 'ADV', re.sub(r'INFN', 'VERB', new_word)))
    return new_word


def get_reply(positive=None, negative=None):  # принимает на вход два списка слов, возвращает одно слово или ошибку
    global model_ru

    if len(positive) == 0 and len(negative) == 0:
        return "Введите хоть что-то!"

    positive = list(map(clean_form, positive))
    negative = list(map(clean_form, negative))

    for word in positive + negative:
        if word not in model_ru:
            return 'Увы, слова "%s" нет в модели!' % word.split('_')[0]

    reply = model_ru.most_similar(negative=negative, positive=positive)[0][0].split('_')[0]

    return reply


if __name__ == '__main__':  # выполнится только один раз при запуске данного скрипта - загрузит модель
    install_model()  # эта модель нормальная, но кажется, когда её обучали, из текста были убраны стоп-слова :(

model_path = 'web_upos_cbow_300_20_2017.bin.gz'  # выполняется каждый раз при запуске программы
model_ru = gensim.models.KeyedVectors.load_word2vec_format(model_path, binary=True)
