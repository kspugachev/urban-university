"""
Домашнее задание по теме "Очереди для обмена данными между потоками".
Цель: применить очереди в работе с потоками, используя класс Queue.
"""
from threading import Thread
from random import randint
from time import sleep
import queue


class Table:
	def __init__(self, number):
		self.number = number  # Номер стола.
		self.guest = None  # Гость за столом (по умолчанию None).


class Guest(Thread):
	def __init__(self, guest_name):
		self.guest_name = guest_name  # Имя гостя.
		super().__init__()

	def run(self):
		sleep(randint(3, 10))  # Ожидание от 3 до 10 секунд.


class Cafe:
	def __init__(self, *tables):
		self.queue = queue.Queue()  # Очередь гостей.
		self.tables = tables  # Столы в кафе.

	def guest_arrival(self, *guests):
		for guest in guests:
			for table in self.tables:
				if table.guest is None:  # Если стол свободен.
					table.guest = guest  # Сажаем гостя за стол.
					guest.start()  # Запускаем поток гостей.
					print(f"{guest.guest_name} сел(-а) за стол номер {table.number}")
					break  # Посадили гостя за стол, перестаем искать свободные столы.

			if not guest.is_alive():  # Если поток гостя закончился.
				self.queue.put(guest)  # Перенаправляем гостей в очередь.
				print(f"{guest.guest_name} в очереди")

	def discuss_guests(self):
		# Пока очередь не пустая или хотя бы один стол занят:
		while not self.queue.empty() or any(table.guest is not None for table in self.tables):
			for table in self.tables:
				if table.guest is not None:  # Если за столом есть гость.
					if not table.guest.is_alive():  # Если гость закончил приём пищи.
						print(f"{table.guest.guest_name} покушал(-а) и ушёл(ушла)")
						table.guest = None  # Освобождаем стол.
						print(f"Стол номер {table.number} свободен")

						if not self.queue.empty():  # Если в очереди есть гости.
							next_guest = self.queue.get()  # Приглашаем следующего гостя из очереди.
							table.guest = next_guest  # Сажаем его за стол.
							next_guest.start()  # Запускаем поток нового гостя.
							print(f"{next_guest.guest_name} вышел(-ла) из очереди и сел(-а) за стол "
								  f"номер {table.number}")
			sleep(1)  # Имитируем обслуживание.


# Создание столов:
tables = [Table(number) for number in range(1, 6)]
# Имена гостей:
guests_names = [
	'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
	'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей:
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами:
cafe = Cafe(*tables)
# Приём гостей:
cafe.guest_arrival(*guests)
# Обслуживание гостей:
cafe.discuss_guests()
