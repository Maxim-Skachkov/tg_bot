import random
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from dotenv import load_dotenv
import os
from utils import help_commands, kb, ikb, kb2, random_photo

load_dotenv()
TOKEN = os.getenv('TOKEN_TG')
bot = Bot(TOKEN)
dp = Dispatcher(bot)


async def rand_ph(message: types.Message):
    photo = random_photo()
    await bot.send_photo(chat_id=message.chat.id,
                         photo=photo[1],
                         caption=f'Ну как фотка <b>{photo[0]}</b>?',
                         parse_mode='HTML',
                         reply_markup=ikb)


async def on_startup(_):
    print("Бот не обрабатывает запросы, которые пришли в оффлайне")


@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text='Привет, я самый классный бот',
                           reply_markup=kb)
    await bot.send_sticker(chat_id=message.from_user.id,
                           sticker='CAACAgIAAxkBAAEHlypj3sDS275bG5Bvyfw1oLjYperkSQACDQEAAladvQpG_UMdBUTXly4E')


@dp.message_handler(commands=['help'])
async def help_handler(message: types.Message):
    text = '<b>Вот что умеет бот:</b>\n'
    for command, info in help_commands.items():
        text += f"<b>{command}</b> - <i>{info}</i>\n"
    await bot.send_message(chat_id=message.from_user.id,
                           text=text,
                           parse_mode='HTML')


@dp.message_handler(commands=['description'])
async def description_handler(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text='Описание еще не придумал, но бот - огонь, это точно!')


@dp.message_handler(commands=['photo'])
async def photo_handler(message: types.Message):
    photo = random_photo()[1]
    await bot.send_photo(chat_id=message.from_user.id,
                         caption='Как тебе фотка?',
                         photo=photo)


@dp.message_handler(Text(equals='Дай фотку'))
async def open_kb(message: types.Message):
    await message.answer(text='Для получения случайной фотки нажми "Хочу смотреть фото!"',
                         reply_markup=kb2)
    await message.delete()


@dp.message_handler(Text(equals='Главное меню'))
async def open_kb(message: types.Message):
    await message.answer(text='Вы находитесь в главном меню',
                         reply_markup=kb)
    await message.delete()


@dp.message_handler(Text(equals='Хочу смотреть фото!'))
async def open_kb2(message: types.Message):
    await rand_ph(message)


@dp.callback_query_handler()
async def callback_handler(callback: types.CallbackQuery):
    if callback.data == 'like':
        await callback.answer('Фотка понравилась!')
    elif callback.data == 'dislike':
        await callback.answer("Фотка не понравилась(((")
    elif callback.data == 'mainmenu':
        await callback.message.answer(text="Вы  в главном меню",
                                      reply_markup=kb)
    elif callback.data == 'next_photo':
        try:
            random_ph = random_photo()
            await callback.message.edit_media(types.InputMedia(media=random_ph[1],
                                                               type='photo',
                                                               caption=random_ph[0]),
                                                                reply_markup=ikb)
        except:
            pass
        await callback.answer()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)