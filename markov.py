from dictogram import Dictogram
import random
#from rethinkdb import RethinkDB
#r = RethinkDB()

def make_markov_model(data):
    markov_model = dict()

    for i in range(0, len(data)-1):
        if data[i] in markov_model:
            # Просто присоединяем к уже существующему распределению
            markov_model[data[i]].update([data[i+1]])
        else:
            markov_model[data[i]] = Dictogram([data[i+1]])
    return markov_model

def make_higher_order_markov_model(data, order=1):
    markov_model = dict()

    for i in range(0, len(data)-order):
        # Создаем окно
        window = tuple(data[i: i+order])
        # Добавляем в словарь
        if window in markov_model:
            # Присоединяем к уже существующему распределению
            markov_model[window].update([data[i+order]])
        else:
            markov_model[window] = Dictogram([data[i+order]])
#        print(markov_model[window])
#        print(window)
    return markov_model

def generate_random_start(model):
    # Чтобы сгенерировать любое начальное слово, раскомментируйте строку:
    # return random.choice(model.keys())

    # Чтобы сгенерировать "правильное" начальное слово, используйте код ниже:
    # Правильные начальные слова - это те, что являлись началом предложений в корпусе
    if 'END' in model:
        seed_word = 'END'
        while seed_word == 'END':
            seed_word = model['END'].return_weighted_random_word()
        return seed_word
#    print(list(model.keys()))
    return random.choice(list(model))

def generate_random_sentence(length, markov_model):
    current_word = generate_random_start(markov_model.keys())
#    print("word")
#    print(current_word)
    sentence = []
    for i in current_word:
        sentence.append(i)
    for i in range(0, length):
        current_dictogram = markov_model[current_word]
        new_tup = list(current_word[1:])
        new_tup.append(current_dictogram.return_weighted_random_word())
        current_word = tuple(new_tup)
        sentence.append(new_tup[-1])
    sentence[0] = sentence[0].capitalize()
    return ' '.join(sentence) + '.'
    return sentence
