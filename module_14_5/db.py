import sqlite3
import config

def initiate_db():
	connection = sqlite3.connect('bot_database.db')
	cursor = connection.cursor()

	cursor.execute('''
	CREATE TABLE IF NOT EXISTS Products(
	id INTEGER PRIMARY KEY,
	title TEXT NOT NULL,
	description TEXT,
	price INTEGER NOT NULL
	);
	''')

	cursor.execute('''
	CREATE TABLE IF NOT EXISTS Users(
	id INTEGER PRIMARY KEY,
	username TEXT NOT NULL,
	email TEXT NOT NULL,
	age INTEGER NOT NULL,
	balance INTEGER NOT NULL 
	);
	''')

	# Фрагмент кода, который вносит информацию в базу данных (если там пусто) из модуля 'config.py':
	cursor.execute("SELECT COUNT(*) FROM Products")
	count = cursor.fetchone()[0]

	if count == 0:
		for i in range(len(config.product_names)):
			cursor.execute('INSERT INTO Products (title, description, price) VALUES(?, ?, ?)',
						   (f'Название: {config.product_names[i]}',
							f'Описание: {config.description[i]}',
							f'Цена: {(i + 1) * 100}'))

	connection.commit()
	connection.close()

# Функция, добавляющая нового пользователя в таблицу 'Users':
def add_user(username, email, age):
	connection = sqlite3.connect('bot_database.db')
	cursor = connection.cursor()
	cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)',
				   (f'{username}', f'{email}', f'{age}', f'{1000}'))
	connection.commit()
	connection.close()

# Функция, проверяющая наличие пользователя в таблице 'Users':
def is_included(username):
	connection = sqlite3.connect('bot_database.db')
	cursor = connection.cursor()
	check_user = cursor.execute('SELECT * FROM Users WHERE username = ?', (username,))
	if check_user.fetchone() is None:
		connection.close()
		return False
	else:
		return True

# Функция, возвращающая все значения таблицы 'Products':
def get_all_products():
	connection = sqlite3.connect('bot_database.db')
	cursor = connection.cursor()

	cursor.execute("SELECT * FROM Products")
	products = cursor.fetchall()

	connection.close()
	return products
