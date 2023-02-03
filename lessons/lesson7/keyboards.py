from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
import os

load_dotenv()
TOKEN = os.getenv('TOKEN_TG')
bot = Bot(TOKEN)
dp = Dispatcher(bot)

kb = ReplyKeyboardMarkup(resize_keyboard=True,
                         one_time_keyboard=True)
buttons = ['/help', '/vote']
b1 = KeyboardButton('/help')
b2 = KeyboardButton('/vote')
kb.add(b1).insert(b2)

ikb = InlineKeyboardMarkup()
ib1 = InlineKeyboardButton(text='👍', callback_data='like')
ib2 = InlineKeyboardButton(text='💩', callback_data='dislike')
ikb.add(ib1, ib2)