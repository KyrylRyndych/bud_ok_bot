from aiogram import types, Dispatcher, Bot
from tg_bot.misc.texts import START_TEXT
from tg_bot.keyboards.reply import create_start_kb


async def start_handler(message: types.message):
    await message.answer(START_TEXT, parse_mode="html", reply_markup=create_start_kb())


def register_start(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands=['start'])
