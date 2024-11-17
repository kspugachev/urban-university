"""
Домашнее задание по теме "Хендлеры обработки сообщений".
"""

from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

api = '**************************************'
bot = Bot(token=api)
dp = Dispatcher(bot, storage = MemoryStorage())

@dp.message_handler(commands=['start'])  # Специфический хендлер, реагирующий на команду.
async def start(message):
	print('Привет! Я бот помогающий твоему здоровью.')

@dp.message_handler()  # Неспецифический хендлер, реагирующий на все сообщения.
async def all_massages(message):
	print('Введите команду /start, чтобы начать общение.')

if __name__ == '__main__':
	executor.start_polling(dp, skip_updates=True)
