from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN_TG')
bot = Bot(TOKEN)
dp = Dispatcher(bot)

ikb = InlineKeyboardMarkup()
ib1 = InlineKeyboardButton(text='google', url='https://www.google.ru/')
ib2 = InlineKeyboardButton(text='yandex', url='https://ya.ru/')
ikb.add(ib1, ib2)


@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await message.answer(text='search engine', reply_markup=ikb)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)