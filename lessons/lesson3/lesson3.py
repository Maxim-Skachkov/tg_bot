import os
from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN_TG')
bot = Bot(TOKEN)
dp = Dispatcher(bot)

stickers = {
    'hot_cherry': 'CAACAgIAAxkBAAEHfExj1SLn5WdWOZQI50pJc9UROir_fwACHAADwDZPE8GCGtMs_g7hLQQ'
}

async def on_startup(_):
    print('yoyoyo')


@dp.message_handler(commands=['start'])
async def start_response(message: types.Message):
    await message.answer(text='<b>Приветики!</b>', parse_mode='HTML')


@dp.message_handler(commands=['sticker'])
async def start_response(message: types.Message):
    await bot.send_sticker(message.from_user.id, sticker=stickers['hot_cherry'])
    await message.delete()


@dp.message_handler()
async def response_message(message: types.Message):
    await message.reply(text='❤️')

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)