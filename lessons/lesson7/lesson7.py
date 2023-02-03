from aiogram import types, executor
from keyboards import kb, bot, dp, ikb


async def on_startup(_):
    print("Let's roll")


@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text='Привет! Я самый лучший бот.',
                           reply_markup=kb)


@dp.message_handler(commands=['help'])
async def help_handler(message: types.Message):
    help_commands = {
        '/help': 'Список всех команд бота',
        '/start': 'Начать работу с ботом заново',
        '/vote': 'Проголосовать за фотки'
    }
    text = '<b>Вот что умеет бот:</b>\n'
    for command, info in help_commands.items():
        text += f"<b>{command}</b> - <i>{info}</i>\n"
    await bot.send_message(chat_id=message.from_user.id,
                           text=text,
                           parse_mode='HTML')


@dp.message_handler(commands=['vote'])
async def vote_handler(message: types.Message):
    await bot.send_photo(chat_id=message.from_user.id,
                         photo='https://www.google.ru/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png',
                         reply_markup=ikb,
                         caption='Фотка норм?')


@dp.callback_query_handler()
async def vote_callback_handler(callback: types.CallbackQuery):
    if callback.data == 'like':
        await callback.answer('Да, фотка класс!')
    elif callback.data == 'dislike':
        await callback.answer('Фотка отстой, согласен!')

if __name__ == '__main__':
    executor.start_polling(dispatcher=dp,
                           skip_updates=True,
                           on_startup=on_startup)
