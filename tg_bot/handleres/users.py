
from aiogram import types, Dispatcher, Bot
from aiogram.dispatcher.filters.builtin import Text
from tg_bot.keyboards.reply import create_start_kb
from tg_bot.misc.texts import START_TEXT, LOCATION_TEXT, OUR_CONTACTS_TEXT
from tg_bot.misc.locations import location


async def start_handler(message: types.message):  #handler start command
    await message.answer(START_TEXT, parse_mode="html", reply_markup=create_start_kb())


async def where_are_we_handler(message: types.message, bot: Bot): # handler for "Where we are"
    await message.answer(LOCATION_TEXT)
    await bot.send_location(chat_id=message.from_user.id, latitude=location['truskav'].latitude, longitude=location['truskav'].longitude)
    await bot.send_location(chat_id=message.from_user.id, latitude=location['zelena'].latitude, longitude=location['zelena'].longitude)


async def our_contacts_handler(message: types.message): # about us handler
    await message.answer(OUR_CONTACTS_TEXT)


async def in_development_handler(message: types.message): # pass handler 
    await message.answer("Ця опція в розробці")


def register_start(dp: Dispatcher):   #register all handlers
    dp.register_message_handler(start_handler, commands=['start'])
    dp.register_message_handler(where_are_we_handler, Text("Де знаходяться магазини"))
    dp.register_message_handler(our_contacts_handler, Text("Наші контакти"))
    dp.register_message_handler(in_development_handler, Text(equals=["Замовити доставку","Мої доставки"]))
    
