import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from config import *
from keyboards import *
import texts

logging.basicConfig(level = logging.INFO)  # Добавим логирование для удобства отладки Телеграм-бота.

bot = Bot(token=API)
dp = Dispatcher(bot, storage = MemoryStorage())

class UserState(StatesGroup):  # Определяем класс для трех состояний.
	age = State()
	growth = State()
	weight = State()


@dp.message_handler(commands=['start'])  # Появляется приветствие и клавиатура при вводе команды '/start'.
async def start(message: types.Message):
	await message.answer(texts.greeting, reply_markup=kb)

@dp.message_handler(text='Рассчитать') # Функция запускается, если нажать кнопку 'Рассчитать' или ввести это слово.
async def main_menu(message: types.Message):
	await message.answer(texts.option, reply_markup=kb_inline) # Появление текста и вложенной клавиатуры.

@dp.message_handler(text='Купить') # Функция запускается, если нажать кнопку 'Купить' или ввести это слово.
async def get_buying_list(message: types.Message):
	for i in range(len(products)):
		with open(f'files/file_{i + 1}.jpg', 'rb') as img:
			await message.answer_photo(img, f'Название: {products[i]} | Описание: {description[i]} | Цена: {(i + 1) * 100}')
	await message.answer(texts.product_choice, reply_markup=kb_inline_2)

# Выводится формула при нажатии на 'Формулы расчета' вложенной клавиатуры:
@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
	await call.message.answer(texts.formula)
	await call.answer()  # Уберем эффект 'западающей' кнопки.

# Выводится сообщение об успешной покупке:
@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
	await call.message.answer(texts.purchase)
	await call.answer()  # Уберем эффект 'западающей' кнопки.

# Функция запускается при нажатии на 'Рассчитать норму калорий' вложенной клавиатуры:
@dp.callback_query_handler(text='calories')
# Запрос на ввод возраста:
async def set_age(call):
	await call.message.answer(texts.age)
	await UserState.age.set()  # Устанавливаем первое состояние ('age').
	await call.answer()  # Уберем эффект 'западающей' кнопки.

@dp.message_handler(state=UserState.age)  # Функция запускается, если установлено первое состояние ('age').
# Обработка ввода возраста и запрос значения роста:
async def set_growth(message: types.Message, state: FSMContext):
	await state.update_data(age=message.text)  # Сохранение значения возраста.
	await message.answer(texts.growth)
	await UserState.growth.set()  # Устанавливаем второе состояние ('growth').

@dp.message_handler(state=UserState.growth)  # Функция запускается, если установлено второе состояние ('growth').
# Обработка ввода роста и запрос значения веса:
async def set_weight(message: types.Message, state: FSMContext):
	await state.update_data(growth=message.text)  # Сохранение значения роста.
	await message.answer(texts.weight)
	await UserState.weight.set()  # Устанавливаем третье состояние ('weight').

@dp.message_handler(state=UserState.weight)  # Функция запускается, если установлено третье состояние ('weight').
# Обработка ввода веса и вывод индивидуальной суточной нормы калорий:
async def send_calories(message: types.Message, state: FSMContext):
	await state.update_data(weight=message.text)  # Сохранение значения веса.
	data = await state.get_data()  # Извлечение ранее сохраненных антропометрических показателей.
	# Вычисление и вывод индивидуальной суточной нормы калорий по формуле Миффлина - Сан Жеора:
	calories = 10 * float(data['weight']) + 6.25 * float(data['growth']) - 5 * int(data['age']) + 5
	await message.answer(f'{texts.calories_norm} {calories}')
	await state.finish()

@dp.message_handler()  # Неспецифический хендлер, реагирующий на все сообщения.
async def all_massages(message):
	await message.answer(texts.start)

if __name__ == '__main__':
	executor.start_polling(dp, skip_updates=True)
