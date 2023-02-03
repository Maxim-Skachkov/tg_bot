from aiogram import Bot, Dispatcher, executor, types
import os
from dotenv import load_dotenv
from keyboards import kb, ikb


load_dotenv()
TOKEN = os.getenv('TOKEN_TG')
bot = Bot(TOKEN)
dp = Dispatcher(bot)

async def on_startup(_):
    print('Я запустился')


@dp.message_handler(commands=['links'])
async def links_handler(message: types.Message):
    await message.reply(reply_markup=ikb, text='Как-то так')


@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await message.reply(reply_markup=kb, text='Вот моя клавиатура!')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)