"""
Домашнее задание по теме "Позиционирование в файле".
"""

def custom_write(file_name, strings):
	string_positions = {}  # Создаем пустой словарь.
	file = open(file_name, 'w', encoding='utf-8')  # Открываем файл для записи. Используем кодировку utf-8.
	str_num = 0

	for i in strings:
		str_num += 1  # Определение номера строки.
		string_positions[str_num, file.tell()] = i  # Формируем элементы словаря.
		file.write(f'{i}\n')  # Записываем строки в файл.

	file.close()
	return string_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
	print(elem)
