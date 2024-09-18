"""
Домашнее задание по теме "Файлы в операционной системе".
"""

import os
import time

directory = r'C:\Users\kspug\MyProjects\urban-university'

for root, dirs, files in os.walk(directory):
	for file in files:
		filepath = os.path.join(root, file) # Полный путь к файлу.
		filetime = os.path.getmtime(filepath) # Время последнего изменения файла.
		formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
		filesize = os.path.getsize(filepath) # Размер файла.
		parent_dir = os.path.dirname(filepath) # Родительская директория файла.
		print(f'Обнаружен файл: {file},'
			  f' Путь: {filepath},'
			  f' Размер: {filesize} байт,'
			  f' Время изменения: {formatted_time},'
			  f' Родительская директория: {parent_dir}')
