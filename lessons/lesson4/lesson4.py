from aiogram import Bot, Dispatcher, executor, types
import os
from dotenv import load_dotenv
import random

load_dotenv()
TOKEN = os.getenv('TOKEN_TG')
bot = Bot(TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['loc'])
async def loc_handler(message: types.Message):
    await bot.send_message(chat_id=message.chat.id, text='Сейчас отправлю в личку')
    latitude = float(f"{random.randrange(1, 99):02}.{random.randrange(0, 999999):06}")
    longtude = float(f"{random.randrange(1, 99):02}.{random.randrange(0, 999999):06}")
    await bot.send_location(chat_id=message.from_user.id, latitude=latitude, longitude=longtude)


@dp.message_handler(commands=['img'])
async def send_img(message: types.Message):
    await bot.send_photo(chat_id=message.from_user.id, photo='https://www.meme-arsenal.com/memes/bd30df10588a61b499197860d88aee73.jpg')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)