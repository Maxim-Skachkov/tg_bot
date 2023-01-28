import os

from aiogram import Bot, Dispatcher, types, executor
import random
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')
bot = Bot(TOKEN)
dp = Dispatcher(bot)

help_text = '''
Список всех команд бота:
/start - начало работы
/help - список всех команд
/description - описание бота, что умеет
'''


@dp.message_handler(commands=['help'])
async def handle_help(message: types.Message):
    await message.reply(text=help_text)


@dp.message_handler(commands=['start'])
async def handle_start(message: types.Message):
    await message.answer(text='Добро пожаловать!')
    await message.delete()


@dp.message_handler(commands=['description'])
async def handle_start(message: types.Message):
    description = 'Очень крутой бот, много всего умеет!!!'
    await message.answer(text=description)


@dp.message_handler()
async def handle_random_letter(message: types.Message):
    letter = random.choice(message.text)
    answer2 = 'YES, THERE IS ZERO IN YOUR MESSAGE' if '0' in message.text else 'NO ONE ZERO HERE'
    await message.answer(text=f'random symbol from your message is... {letter} !!!')
    await message.answer(text=answer2)


if __name__ == '__main__':
    executor.start_polling(dp)