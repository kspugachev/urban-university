from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Создаем обычную клавиатуру:
kb = ReplyKeyboardMarkup(resize_keyboard=True)  # Подстраиваем клавиатуру под размер экрана устройства.
button_1 = KeyboardButton(text='Рассчитать')
kb.add(button_1)
button_2 = KeyboardButton(text='Информация')  # Кнопка не наделена функционалом.
kb.add(button_2)
button_5 = KeyboardButton(text='Купить')
kb.add(button_5)

# Создаем Inline клавиатуру:
kb_inline = InlineKeyboardMarkup()
button_3 = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
kb_inline.add(button_3)
button_4 = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
kb_inline.add(button_4)

# Создаем Inline клавиатуру для выбора покупки:
kb_inline_2 = InlineKeyboardMarkup()
button_6 = InlineKeyboardButton(text='Продукт №1', callback_data='product_buying')
kb_inline_2.add(button_6)
button_7 = InlineKeyboardButton(text='Продукт №2', callback_data='product_buying')
kb_inline_2.add(button_7)
button_8 = InlineKeyboardButton(text='Продукт №3', callback_data='product_buying')
kb_inline_2.add(button_8)
button_9 = InlineKeyboardButton(text='Продукт №4', callback_data='product_buying')
kb_inline_2.add(button_9)
