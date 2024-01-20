'''
Знакомство с языком Python (семинары)
Урок 10. Построение графиков
Задача 44: В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца. 
Ваша задача перевести его в one hot вид. Сделать без встроенных ф-ций, например,get_dummies?
'''

import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()

# Внесение дополнительного кода решения согласно поставленной задачи
data.loc[data['whoAmI'] == 'robot', 'robot'] = '1'
data.loc[data['whoAmI'] == 'human', 'human'] = '1'
data.loc[(data['whoAmI'] == 'robot') & (data['robot'] == '1'), 'human'] = '0'
data.loc[(data['whoAmI'] == 'human') & (data['human'] == '1'), 'robot'] = '0'
data.drop('whoAmI', axis=1, inplace=True)


print(data)
