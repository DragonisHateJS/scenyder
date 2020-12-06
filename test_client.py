#from markov import make_higher_order_markov_model, generate_random_sentence
import markov
import csv
import re

plots = {} 
with open("pritr.csv", "r", newline="") as file:
    for p in csv.reader(file, delimiter = ","):
        plots[p[1]] = p[2]
data = []
for i in plots.values():
    for j in i.lower().split():
        data.append(j)
for i in range(len(data)):
    data[i] = re.sub(r"[\.\,\—\?\!]+", "", data[i])
    if data[i] == 'end':
        data[i] = data[i].upper()
#ЗДЕСЬ ВАША - КЛИЕНТСКАЯ ЧАСТЬ
#В КАЧЕСТВА АРГУМЕНТОВ ПЕРЕДАЮТСЯ СЛОВА ДЛЯ МАРКОВСКОЙ ЦЕПИ И
#КОЛ-ВО СЛОВ ДЛЯ СВЯЗЫВАНИЯ (2 - ПОКА ОПТИМАЛЬНЫЙ ВАРИАНТ, Т.К. ЕСЛИ СТАВИТЬ 1,
#ТО БУДЕТ БУРДА, ЕСЛИ СТАВИТЬ 3, ТО ОН БУДЕТ ТУПО КОПИРОВАТЬ ОДИН СИНОПСИС)
model = make_higher_order_markov_model(data, 2)
#ЗДЕСЬ АРГУМЕНТЫ - КОЛ-ВО СЛОВ В ПРЕДЛОЖЕНИИ И МОДЕЛЬ
#ВАМ НУЖНО ТОЛЬКО КОЛ-ВО СЛОВ
print(generate_random_sentence(40, model))