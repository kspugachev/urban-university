"""
Домашнее задание по теме "Выбор элементов и функции в SQL запросах".
Цель: научится использовать функции внутри запросов языка SQL и использовать их в решении задачи.
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
				   (f'User{i}', f'example{i}@gmail.com', f'{10 * i}', 1000))

# Обновляем 'balance' у каждой 2ой записи начиная с 1ой на 500:
cursor.execute('UPDATE Users SET balance = ? WHERE id%2 != 0', (500,))

# Удаляем каждую 3ую запись в таблице начиная с 1ой:
cursor.execute('DELETE FROM Users WHERE (id + 2)%3 == 0')

# Выводим на консоль записи, где возраст не равен 60:
cursor.execute('SELECT * FROM Users WHERE age != 60')

# Удаляем пользователя с id=6:
cursor.execute('DELETE FROM Users WHERE id = ?', (6, ))

# Подсчитываем количество всех пользователей:
cursor.execute('SELECT COUNT(*) FROM Users')
total_users = cursor.fetchone()[0]

# Подсчитываем сумму всех балансов:
cursor.execute('SELECT SUM(balance) FROM Users')
all_balances = cursor.fetchone()[0]

# Выводим на консоль среднее арифметическое балансов пользователей (1-й вариант):
print(all_balances / total_users)

#  Выводим на консоль среднее арифметическое балансов пользователей (2-й вариант):
cursor.execute('SELECT AVG(balance) FROM Users')
print(cursor.fetchone()[0])

connection.commit()
connection.close()
