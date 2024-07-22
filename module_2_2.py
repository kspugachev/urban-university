"""
Домашняя работа по уроку "Условная конструкция. Операторы if, elif, else".
Цель: применить навыки создания условных конструкций и знания операторов if, else, elif / and, or, not.
"""

first = int(input('Введите первое целое число: '))
second = int(input('Введите второе целое число: '))
third = int(input('Введите третье целое число: '))

if first == second == third:
    print(3)
elif first == second or first == third or second == third:
    print(2)
else:
    print(0)
