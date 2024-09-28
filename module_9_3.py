"""
Домашнее задание по теме "Генераторные сборки".
Цель: понять механизм создания генераторных сборок и использования встроенных функций-генераторов.
"""

first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (abs(len(x) - len(y)) for x, y in zip(first, second) if len(x) != len(y))
second_result = (len(first[i]) == len(second[i]) for i in range(len(first)))
# Альтернативный вариант без использования len() и range():
# second_result = (len(x) == len(y) for x in first for y in second if first.index(x) == second.index(y))

print(list(first_result))
print(list(second_result))
