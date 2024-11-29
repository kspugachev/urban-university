"""
Домашнее задание по теме "Создание БД, добавление, выбор и удаление элементов".
Цель: освоить основные команды языка SQL и использовать их в коде используя SQLite3.
"""

import sqlite3

# Создаем соединение для работы с базой данных:
connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

# Создаем таблицу:
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

# Вносим данные 10ти пользователей в таблицу:
for i in range (1, 11):
	cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES(?,?,?, ?)',
				   (f'User{i}', f'example{i}@gmail.com', f'{10 * i}', '1000'))

# Обновляем 'balance' у каждой 2ой записи начиная с 1ой на 500:
cursor.execute('UPDATE Users SET balance = ? WHERE id%2 != 0', ('500',))

# Удаляем каждую 3ую запись в таблице начиная с 1ой:
cursor.execute('DELETE FROM Users WHERE (id + 2)%3 == 0')

# Выводим на консоль записи, где возраст не равен 60:
cursor.execute('SELECT * FROM Users WHERE age != 60')
users = cursor.fetchall()
for user in users:
	print(f'Имя: {user[1]} | Почта: {user[2]} | Возраст: {user[3]} | Баланс: {user[4]}')

connection.commit()
connection.close()
