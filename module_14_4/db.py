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

def get_all_products():
	connection = sqlite3.connect('bot_database.db')
	cursor = connection.cursor()

	cursor.execute("SELECT * FROM Products")
	products = cursor.fetchall()

	connection.close()
	return products
