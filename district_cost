import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv

x, y, districts = [], [], []

with open("districts_cost.csv") as file:
    reader = csv.reader(file, delimiter=';')
    for line in reader:
        districts.append(line[0])
        x.append(int(line[1]))
        y.append(int(line[2]))


xy = range(len(districts))

# Помещаем кортеж, содержащий фигуру и объект осей в переменные
fig, ax = plt.subplots() #plt.subplots() - это функция, которая возвращает кортеж, содержащий фигуру и объект осей. 

plt.scatter(xy, x, label=u'однокомнатные', color='b')
plt.scatter(xy, y, label=u'двухкомнатные', color='r')

plt.xlabel('Районы Санкт-Петербурга')
plt.ylabel('Цена')
plt.title('Cтоимость квартир по районам СПб')
plt.xticks(xy, districts)
fig.autofmt_xdate(rotation=45) #убирает смещение ,поворачивая метки по x
plt.legend()
plt.savefig('img.png', format='png')
plt.show()
