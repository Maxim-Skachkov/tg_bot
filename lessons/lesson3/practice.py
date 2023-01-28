import os
from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv

load_dotenv()

bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher(bot)
stickers = {
    'hot_cherry': 'CAACAgIAAxkBAAEHfExj1SLn5WdWOZQI50pJc9UROir_fwACHAADwDZPE8GCGtMs_g7hLQQ',
    'cat': 'CAACAgIAAxkBAAEHfhNj1YoWBpH3MMpv7w5XAAG2_K5bea8AArIMAAJHbdFLadSmkPiPjistBA',

}

help_dict = {
    '/help': 'Все команды бота',
    '/give': 'Получить стикер с котиком',
}


async def on_startup(_):
    print("Я запустился!")


@dp.message_handler(commands=['help'])
async def help_handler(message: types.Message):
    reply_text = ''
    for command, description in help_dict.items():
        reply_text += f"<b>{command}</b> - <i>{description}</i>\n"
    await message.answer(text=reply_text, parse_mode='HTML')


@dp.message_handler(commands=['give'])
async def give_handler(message: types.Message):
    await message.answer(text='Смотри какой смешной кот ❤')
    await bot.send_sticker(message.from_user.id, sticker=stickers.get('cat'))


@dp.message_handler()
async def heart_reply(message: types.Message):
    if '❤' in message.text:
        await message.reply(text='🖤')
    checks_count = message.text.count('✅')
    if checks_count > 0:
        await message.reply(text=f"There's {checks_count} checks in your message")


@dp.message_handler(content_types=['sticker'])
async def send_sticker_id(message:types.Message):
    await message.answer(text=f"Sticker's ID is \n{message.sticker.file_id}")

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)