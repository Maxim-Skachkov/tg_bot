from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

ikb = InlineKeyboardMarkup(row_width=3)
ib1 = InlineKeyboardButton(text='google', url='https://www.google.ru/')
ib2 = InlineKeyboardButton(text='yandex', url='https://ya.ru/')
ikb.add(ib1, ib2)

kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
b1 = KeyboardButton('/links')
kb.add(b1)