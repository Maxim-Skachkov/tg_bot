from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
import os
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton

load_dotenv()

TOKEN = os.getenv('TOKEN_TG')
bot = Bot(TOKEN)
dp = Dispatcher(bot)

kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
buttons = {
    'help': KeyboardButton('/help'),
    'loc': KeyboardButton('/loc'),
    'description': KeyboardButton('/description'),
    'img': KeyboardButton('/img'),
}
[kb.insert(btn) if loop_count % 2 else kb.add(btn) for loop_count, btn in enumerate(buttons.values())]

HELP = {
    '/help': 'Запрос помощи',
    '/description': 'Описание бота',
    '/img': 'Запросить картинку',
    '/loc': 'Получить местоположение бункера'
}


async def del_msg(message):
    if message.from_user.id != message.chat.id:
        await message.delete()


async def on_startup(_):
    print('ПОЕХАЛИ')


@dp.message_handler(commands=['help'])
async def help_handler(message: types.Message):
    help_text = ''
    for command, description in HELP.items():
        help_text += f"<b>{command}</b> - <i>{description}</i>\n"
    await bot.send_message(chat_id=message.from_user.id, text=help_text, parse_mode='HTML')
    await del_msg(message)


@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    welcome_text = 'Привет! Наш бот классный. Для получения списка команд пиши /help'
    await bot.send_message(chat_id=message.from_user.id, text=welcome_text, reply_markup=kb)
    await bot.send_message(chat_id=message.from_user.id, text=f"Hello, your ID is {message.from_user.id}")
    await del_msg(message)


@dp.message_handler(commands=['description'])
async def description_handler(message: types.Message):
    descr_text = 'Бот умеет отправлять смешную фотку, а также подскажет где искать бункер'
    await bot.send_message(chat_id=message.from_user.id, text=descr_text)
    await del_msg(message)


@dp.message_handler(commands=['loc'])
async def loc_handler(message: types.Message):
    text = 'Ищи бункер ТУТ!'
    await bot.send_message(chat_id=message.from_user.id, text=text)
    await bot.send_location(chat_id=message.from_user.id, latitude=61.716003, longitude=31.911356)
    await del_msg(message)


@dp.message_handler(commands=['img'])
async def img_handler(message: types.Message):
    photo_url = 'https://s12.stc.yc.kpcdn.net/share/i/12/12356784/wr-960.webp'
    await bot.send_photo(chat_id=message.from_user.id, photo=photo_url)
    await del_msg(message)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
