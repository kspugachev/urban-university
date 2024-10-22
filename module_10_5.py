"""
Домашнее задание по теме "Многопроцессное программирование".
Цель: понять разницу между линейным и многопроцессным подходом, выполнив операции обоими способами.
"""

import datetime
import multiprocessing

def read_info(name):
	all_data = []
	with open(name, 'r', encoding='utf-8') as data:
		for line in data:  # Читаем файл построчно.
			all_data.append(line.strip())  # Добавляем 'очищенную' строку в список.

		# Альтернативный вариант перебора строк в файле с использованием readline (согласно требованиям задачи):
		# while True:
		# 	line = data.readline()
		# 	all_data.append(line.strip())
		# 	if not line:
		# 		break

filenames = [f'./file {number}.txt' for number in range(1, 5)]  # Создание списка названий файлов.

# Фрагмент кода для линейного вызова:
# start = datetime.datetime.now()
# for file in filenames:
# 	read_info(file)
# end = datetime.datetime.now()
#
# print(end - start)

# Фрагмент кода для многопроцессного вызова:
if __name__ == '__main__':
	with multiprocessing.Pool(processes=2) as pool:
		start = datetime.datetime.now()
		pool.map(read_info, filenames)
		end = datetime.datetime.now()

	print(end - start)
