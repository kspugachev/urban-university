"""
Домашнее задание по теме "Методы отправки сообщений".
"""

from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

api = '**************************************'
bot = Bot(token=api)
dp = Dispatcher(bot, storage = MemoryStorage())

@dp.message_handler(commands=['start'])  # Специфический хендлер, реагирующий на команду.
async def start(message):
	await message.answer('Привет! Я бот помогающий твоему здоровью.')

# Пробуем создать неспецифический "эхо-бот", который будет отвечать словами (в верхнем регистре) пользователя:
# @dp.message_handler()
# async def all_massages(message):
# 	await message.answer(message.text.upper())

@dp.message_handler()  # Неспецифический хендлер, реагирующий на все сообщения.
async def all_massages(message):
	await message.answer('Введите команду /start, чтобы начать общение.')

if __name__ == '__main__':
	executor.start_polling(dp, skip_updates=True)
