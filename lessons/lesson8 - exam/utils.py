import random

from aiogram.types import KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup

help_commands = {
    '/help': 'Список всех команд бота',
    '/start': 'Начать работу с ботом заново',
    '/description': 'Описание бота',
    '/photo': 'Оценить случайную фотку',
    'Дай фотку': 'Посмотреть случайное фото'
}

kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
[kb.insert(KeyboardButton(cmd)) if count % 2 else kb.add(KeyboardButton(cmd))
 for count, cmd in enumerate(help_commands)]

ikb = InlineKeyboardMarkup()
ib1 = InlineKeyboardButton(text='Следующая фотка', callback_data='next_photo')
ib2 = InlineKeyboardButton(text='Супер!', callback_data='like')
ib3 = InlineKeyboardButton(text='Кал!', callback_data='dislike')
ib4 = InlineKeyboardButton(text='Главное меню', callback_data='mainmenu')
ikb.add(ib1, ib2, ib3, ib4)

kb2 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb2b1 = KeyboardButton(text='Главное меню')
kb2b2 = KeyboardButton(text="Хочу смотреть фото!")
kb2.add(kb2b1, kb2b2)


def random_photo():
    photos = {
        'google': 'https://www.google.ru/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png',
        'bonch1': 'https://www.sut.ru/new_site/images/news/1675424228.jpg',
        'bonch2': 'https://www.sut.ru/new_site/images/news/1675254825.jpg',
        'bonch3': 'https://www.sut.ru/new_site/images/news/1675409593.jpg',
    }

    return random.choice(tuple(photos.items()))

