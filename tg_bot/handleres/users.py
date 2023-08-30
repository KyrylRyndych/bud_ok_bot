from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove

from tg_bot.keyboards.reply import create_start_kb, create_cancel_kb
from tg_bot.misc.texts import REG_HELP_TEXT
from tg_bot.models.sqlite import Sql_user_tb
from tg_bot.misc.FSM import Register_UserState


async def help_command(message: types.Message):
    await message.answer(text=REG_HELP_TEXT)


async def user_start(message: types.Message):
    await message.answer("Чтобы использовать бота нужно зарегестрироваться: /register\n помощь: /help",
                         reply_markup=create_start_kb())


async def register_command(message: types.Message, user_tb: Sql_user_tb):
    await Register_UserState.name.set()
    await message.answer("Как вас зовут? (Имя, Фамилия)", reply_markup=create_cancel_kb())
    user_tb.create_user_table()


async def cancel_command(message: types.Message, state: FSMContext):
    await state.finish()
    await message.reply("Вы отменили регестрацию", reply_markup=create_start_kb())


async def check_name(message: types.Message):
    return await message.answer("Неправильный ввод. Введите: Имя Фамилия")


async def save_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await Register_UserState.next()
    await message.answer("Введите ваш номер телефона. Формат: 380ХХХХХХХХХ")


async def check_phone(message: types.Message):
    await message.reply("Неверный номер. Формат: 380ХХХХХХХХХ")


async def save_phone(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['phone'] = f'+{message.text}'
    await Register_UserState.next()
    await message.answer("Укажите ваш email")


async def check_email(message: types.Message):
    await message.reply("Неверный email. Попробуйт снова")


async def save_email(message: types.Message, state: FSMContext, user_tb: Sql_user_tb):
    async with state.proxy() as data:
        data['email'] = message.text
        user_tb.add_user(id=message.from_user.id, name=data['name'],
                         phone=data['phone'], email=data['email'])
    await message.answer("Вы успешно зарегестрировались", reply_markup=ReplyKeyboardRemove())
    await state.finish()


def register_user(dp: Dispatcher):
    dp.register_message_handler(help_command, commands=['help'])
    dp.register_message_handler(user_start, commands=['start'])
    dp.register_message_handler(register_command, commands=['register'])
    dp.register_message_handler(cancel_command, commands=['cancel'], state="*")
    dp.register_message_handler(check_name,
                                lambda message: not message.text.count(' ') == 1, state=Register_UserState.name)
    dp.register_message_handler(save_name, state=Register_UserState.name)
    dp.register_message_handler(check_phone,
                                lambda message: not message.text.startswith("380") or not message.text.isdigit()
                                                or not len(message.text) == 12,
                                state=Register_UserState.phone)
    dp.register_message_handler(save_phone, state=Register_UserState.phone)
    dp.register_message_handler(check_email,
                                lambda message: not message.text.count('@'), state=Register_UserState.email)
    dp.register_message_handler(save_email, state=Register_UserState.email)
