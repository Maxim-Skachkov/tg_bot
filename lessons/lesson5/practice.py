from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
import random
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN_TG')
bot = Bot(TOKEN)
dp = Dispatcher(bot)

HELP = {
    '/help': 'Запрос помощи',
    '/description': 'Описание бота',
}
kb = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
buttons = {
    'help': KeyboardButton('/help'),
    'description': KeyboardButton('/description'),
    'heart': KeyboardButton('❤️'),
    '/orange': KeyboardButton('/orange'),
    '/loc': KeyboardButton('/loc'),
}
[kb.insert(btn) if loop_counter % 3 else kb.add(btn) for loop_counter, btn in enumerate(buttons.values())]

kb2 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb2.add(KeyboardButton('/'))


async def del_msg(message):
    if message.from_user.id != message.chat.id:
        await message.delete()


@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           reply_markup=kb,
                           text='Приветики!')
    await message.delete()


@dp.message_handler(commands=['help'])
async def help_handler(message: types.Message):
    text = ''
    for command, description in HELP.items():
        text += f"<b>{command}</b> - <i>{description}</i>\n"
    await bot.send_message(chat_id=message.from_user.id, text=text, parse_mode='HTML')
    await del_msg(message)


@dp.message_handler(commands=['description'])
async def descr_handler(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text='Клевый бот! Описание потом придумаю')
    await del_msg(message)


@dp.message_handler(commands=['orange'])
async def orange_handler(message: types.Message):
    photo_url = 'https://5.imimg.com/data5/VN/YP/MY-33296037/orange-600x600-500x500.jpg'
    await bot.send_photo(chat_id=message.chat.id, photo=photo_url)
    await del_msg(message)


@dp.message_handler(commands=['loc'])
async def loc_handler(message: types.Message):
    latitude = float(f"{random.randrange(1, 99):02}.{random.randrange(0, 999999):06}")
    longtude = float(f"{random.randrange(1, 99):02}.{random.randrange(0, 999999):06}")
    await bot.send_location(chat_id=message.from_user.id, latitude=latitude, longitude=longtude)
    await del_msg(message)


@dp.message_handler()
async def heart_reply(message: types.Message):
    cat_sticker = 'CAACAgIAAxkBAAEHiIFj2WF31YEBVkHyShSq51ORpR8EEwACdQADmL-ADanCRvzcThmRLQQ'
    if '❤' in message.text:
        await bot.send_sticker(chat_id=message.from_user.id, sticker=cat_sticker)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
