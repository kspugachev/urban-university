"""
Домашнее задание по теме "Генераторы".
Цель: более глубоко понять особенности работы с функциями-генераторами и оператором yield в Python.
"""

def all_variants(text):
	length = len(text)  # Длина начальной строки.
	for size in range(1, length + 1):  # Варианты длин строк.
		for start_index in range(length - size + 1):  # Варианты первого значения строк.
			yield text[start_index:start_index + size]  # Выводим последовательность строк.

a = all_variants('abc')
for i in a:
	print(i)
