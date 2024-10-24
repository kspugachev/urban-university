"""
Домашнее задание по теме "Обзор сторонних библиотек Python".
Цель: познакомиться с использованием сторонних библиотек в Python и применить их в различных задачах.
"""

import requests
import numpy as np
import pandas as pd

# URL для запроса (воспользуемся данными с Московской биржи):
url = 'https://iss.moex.com/iss/statistics/engines/currency/markets/selt/rates.json'

response = requests.get(url)  # Выполнение get-запроса.

if response.status_code == 200:  # Проверка успешности запроса.
	data = response.json()  # Вызываем метод json().

	# Извлечение курса доллара, его изменения и даты торгов:
	usd = data['cbrf']['data'][0][3]  # Индекс 3 соответствует 'CBRF_USD_LAST' (курс доллара).
	usd_change = data['cbrf']['data'][0][4]  # Индекс 4 соответствует 'CBRF_USD_LASTCHANGEPRCNT' (% изменения).
	usd_date = data['cbrf']['data'][0][5]  # Индекс 5 соответствует 'CBRF_USD_TRADEDATE' (дата торгов).

	# Извлечение курса евро, его изменения и даты торгов:
	eur = data['cbrf']['data'][0][6]  # Индекс 6 соответствует 'CBRF_EUR_LAST' (курс евро).
	eur_change = data['cbrf']['data'][0][7]  # Индекс 7 соответствует 'CBRF_EUR_LASTCHANGEPRCNT' (% изменения).
	eur_date = data['cbrf']['data'][0][8]  # Индекс 8 соответствует 'CBRF_EUR_TRADEDATE' (дата торгов).

	def rate_change(change):
		if change < 0:
			return f'уменьшился на'
		elif change > 0:
			return f'увеличился на'
		else:
			return f'не изменился:'

	print()
	print(f"Курс доллара: {usd} руб. по состоянию на {usd_date} (курс {rate_change(usd_change)} {abs(usd_change)} руб.)")
	print(f"Курс евро: {eur} руб. по состоянию на {eur_date} (курс {rate_change(eur_change)} {abs(eur_change)} руб.)")

	# Выводим данные в табличной форме при помощи библиотеки Pandas:
	print()
	print('************************************************')
	print(pd.DataFrame({f'Курс валюты на {usd_date}': [usd, eur], 'Изменение курса': [usd_change, eur_change]},
					   index = ['USD', 'EURO']))
else:
	print(f"Ошибка при получении данных: {response.status_code}")

# Воспользуемся библиотеками NumPy и Pandas, построим таблицу (10 строк, 5 столбцов) из случайных значений:
print()
print('***************************************************')
df = pd.DataFrame(np.random.randn(10, 5), columns=list("ABCDE"))
print(df)

# Выводим основные статистические данные табличных значений:
print()
print('************************************************************')
print(df.describe())

# Отсортируем значения в колонке 'A' в порядке убывания:
print()
print('***************************************************')
df_new = df.sort_values(by="A", ascending=False)
print(df_new)

# Создадим файл в формате .csv содержащий табличные данные:
df_new.to_csv("example.csv")
