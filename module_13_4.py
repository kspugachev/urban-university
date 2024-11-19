"""
Домашнее задание по теме "Машина состояний".
"""

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup


api = '********************************************'
bot = Bot(token=api)
dp = Dispatcher(bot, storage = MemoryStorage())

class UserState(StatesGroup):  # Определяем класс для трех состояний.
	age = State()
	growth = State()
	weight = State()

@dp.message_handler(text='Calories')  # Функция запускается, если пользователь ввел 'Calories'.
# Запрос на ввод возраста:
async def set_age(message: types.Message):  # Указываем типы аргументов (аннотация типов).
	await message.answer('Введите свой возраст:')
	await UserState.age.set()  # Устанавливаем первое состояние ('age').

@dp.message_handler(state=UserState.age)  # Функция запускается, если установлено первое состояние ('age').
# Обработка ввода возраста и запрос значения роста:
async def set_growth(message: types.Message, state: FSMContext):  # Указываем типы аргументов (аннотация типов).
	await state.update_data(age=message.text)  # Сохранение значения возраста.
	await message.answer('Введите свой рост:')
	await UserState.growth.set()  # Устанавливаем второе состояние ('growth').

@dp.message_handler(state=UserState.growth)  # Функция запускается, если установлено второе состояние ('growth').
# Обработка ввода роста и запрос значения веса:
async def set_weight(message: types.Message, state: FSMContext):  # Указываем типы аргументов (аннотация типов).
	await state.update_data(growth=message.text)  # Сохранение значения роста.
	await message.answer('Введите свой вес:')
	await UserState.weight.set()  # Устанавливаем третье состояние ('weight').

@dp.message_handler(state=UserState.weight)  # Функция запускается, если установлено третье состояние ('weight').
# Обработка ввода веса и вывод индивидуальной суточной нормы калорий:
async def send_calories(message: types.Message, state: FSMContext):  # Указываем типы аргументов (аннотация типов).
	await state.update_data(weight=message.text)  # Сохранение значения веса.
	data = await state.get_data()  # Извлечение ранее сохраненных антропометрических показателей.
	# Вычисление и вывод индивидуальной суточной нормы калорий по формуле Миффлина - Сан Жеора:
	calories = 10 * float(data['weight']) + 6.25 * float(data['growth']) - 5 * int(data['age']) + 5
	await message.answer(f'Ваша норма калорий {calories}')
	await state.finish()

if __name__ == '__main__':
	# При запуске бот игнорирует старые сообщения в чате и реагирует только на новые:
	executor.start_polling(dp, skip_updates=True)
