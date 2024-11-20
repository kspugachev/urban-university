"""
Домашнее задание по теме "Клавиатура кнопок".
"""

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


api = '**********************************************'
bot = Bot(token=api)
dp = Dispatcher(bot, storage = MemoryStorage())

# Создаем клавиатуру с двумя кнопками:
kb = ReplyKeyboardMarkup(resize_keyboard=True)  # Подстраиваем клавиатуру под размер экрана устройства.
button_1 = KeyboardButton(text='Рассчитать')
kb.add(button_1)
button_2 = KeyboardButton(text='Информация')  # Кнопка не наделена функционалом.
kb.add(button_2)

class UserState(StatesGroup):  # Определяем класс для трех состояний.
	age = State()
	growth = State()
	weight = State()


@dp.message_handler(commands=['start'])  # Появляется приветствие и клавиатура при вводе команды '/start'.
async def start(message: types.Message):
	await message.answer('Привет! Я бот, помогающий твоему здоровью.', reply_markup=kb)

@dp.message_handler(text='Рассчитать')  # Функция запускается, если нажать кнопку 'Рассчитать' или ввести это слово.
# Запрос на ввод возраста:
async def set_age(message: types.Message):
	await message.answer('Введите свой возраст:')
	await UserState.age.set()  # Устанавливаем первое состояние ('age').

@dp.message_handler(state=UserState.age)  # Функция запускается, если установлено первое состояние ('age').
# Обработка ввода возраста и запрос значения роста:
async def set_growth(message: types.Message, state: FSMContext):
	await state.update_data(age=message.text)  # Сохранение значения возраста.
	await message.answer('Введите свой рост:')
	await UserState.growth.set()  # Устанавливаем второе состояние ('growth').

@dp.message_handler(state=UserState.growth)  # Функция запускается, если установлено второе состояние ('growth').
# Обработка ввода роста и запрос значения веса:
async def set_weight(message: types.Message, state: FSMContext):
	await state.update_data(growth=message.text)  # Сохранение значения роста.
	await message.answer('Введите свой вес:')
	await UserState.weight.set()  # Устанавливаем третье состояние ('weight').

@dp.message_handler(state=UserState.weight)  # Функция запускается, если установлено третье состояние ('weight').
# Обработка ввода веса и вывод индивидуальной суточной нормы калорий:
async def send_calories(message: types.Message, state: FSMContext):
	await state.update_data(weight=message.text)  # Сохранение значения веса.
	data = await state.get_data()  # Извлечение ранее сохраненных антропометрических показателей.
	# Вычисление и вывод индивидуальной суточной нормы калорий по формуле Миффлина - Сан Жеора:
	calories = 10 * float(data['weight']) + 6.25 * float(data['growth']) - 5 * int(data['age']) + 5
	await message.answer(f'Ваша норма калорий {calories}')
	await state.finish()

if __name__ == '__main__':
	executor.start_polling(dp, skip_updates=True)
