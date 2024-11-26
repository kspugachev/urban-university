"""
Домашнее задание по теме "Inline клавиатуры".
Цель: научится создавать Inline клавиатуры и кнопки на них в Telegram-bot.
"""

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


api = '****************************************'
bot = Bot(token=api)
dp = Dispatcher(bot, storage = MemoryStorage())

# Создаем клавиатуру с двумя кнопками:
kb = ReplyKeyboardMarkup(resize_keyboard=True)  # Подстраиваем клавиатуру под размер экрана устройства.
button_1 = KeyboardButton(text='Рассчитать')
kb.add(button_1)
button_2 = KeyboardButton(text='Информация')  # Кнопка не наделена функционалом.
kb.add(button_2)

# Создаем Inline клавиатуру:
kb_inline = InlineKeyboardMarkup()
button_3 = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
kb_inline.add(button_3)
button_4 = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
kb_inline.add(button_4)

class UserState(StatesGroup):  # Определяем класс для трех состояний.
	age = State()
	growth = State()
	weight = State()


@dp.message_handler(commands=['start'])  # Появляется приветствие и клавиатура при вводе команды '/start'.
async def start(message: types.Message):
	await message.answer('Привет! Я бот, помогающий твоему здоровью.', reply_markup=kb)

@dp.message_handler(text='Рассчитать') # Функция запускается, если нажать кнопку 'Рассчитать' или ввести это слово.
async def main_menu(message: types.Message):
	await message.answer('Выберите опцию:', reply_markup=kb_inline) # Появление текста и вложенной клавиатуры.

# Выводится формула при нажатии на 'Формулы расчета' вложенной клавиатуры:
@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
	await call.message.answer('10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5')
	await call.answer()  # Уберем эффект 'западающей' кнопки.

# Функция запускается при нажатии на 'Рассчитать норму калорий' вложенной клавиатуры:
@dp.callback_query_handler(text='calories')
# Запрос на ввод возраста:
async def set_age(call):
	await call.message.answer('Введите свой возраст:')
	await UserState.age.set()  # Устанавливаем первое состояние ('age').
	await call.answer()  # Уберем эффект 'западающей' кнопки.

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

@dp.message_handler()  # Неспецифический хендлер, реагирующий на все сообщения.
async def all_massages(message):
	await message.answer('Введите команду /start, чтобы начать общение.')

if __name__ == '__main__':
	executor.start_polling(dp, skip_updates=True)



