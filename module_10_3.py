"""
Домашнее задание по теме "Блокировки и обработка ошибок".
Цель: освоить блокировки потоков, используя объекты класса Lock и его методы.
"""

import threading
import random
import time


class Bank:
	def __init__(self):
		self.balance = 0  # Изначальный баланс.
		self.lock = threading.Lock()

	def deposit(self):
		for transaction in range(100):  # 100 транзакций (пополнение средств).
			put_money = random.randint(50, 500)  # Пополнение на случайную сумму от 50 до 500.

			if self.balance >= 500 and self.lock.locked():  # Условие: если баланс более 500 и замок заблокирован.
				self.lock.release()  # Разблокировка замка.

			self.balance += put_money  # Пополнение баланса.
			print(f'Пополнение: {put_money}. Баланс: {self.balance}')

			time.sleep(0.001)  # Имитация обработки запроса.

	def take(self):
		for transaction in range(100):  # 100 транзакций (снятие средств)
			take_money = random.randint(50, 500)  # Снятие случайной суммы от 50 до 500.
			print(f'Запрос на {take_money}')

			if take_money <= self.balance:  # Проверка на наличие достаточного количества средств на балансе.
				self.balance -= take_money  # Снятие средств.
				print(f'Снятие: {take_money}. Баланс: {self.balance}')
			else:
				print(f'Запрос отклонён, недостаточно средств')
				self.lock.acquire()  # Блокировка замка.

			time.sleep(0.001)  # Имитация обработки запроса.


# Создание объекта класса Bank.
bk = Bank()

# Создание потоков.
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

# Запуск потоков.
th1.start()
th2.start()
# Остановка потоков.
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
