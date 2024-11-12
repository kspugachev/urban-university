"""
Домашнее задание по теме "Асинхронность на практике".
"""

import asyncio


async def start_strongman(name, power):  # Создаем корутину (асинхронную функцию).
	print(f'Силач {name} начал соревнования')

	for ball_number in range(1, 6):
		await asyncio.sleep(1 / power)  # Задержка обратно пропорциональна значению силы.
		print(f'Силач {name} поднял {ball_number}')

	print(f'Силач {name} закончил соревнования')


async def start_tournament():  # Создаем корутину (асинхронную функцию).
	# Формируем ряд задач:
	task1 = asyncio.create_task(start_strongman('Pasha', 3))
	task2 = asyncio.create_task(start_strongman('Denis', 4))
	task3 = asyncio.create_task(start_strongman('Apollon', 5))
	# Ожидаем завершения всех запущенных задач:
	await task1
	await task2
	await task3


# Запуск асинхронной функции:
asyncio.run(start_tournament())
