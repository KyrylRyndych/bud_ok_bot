from aiogram import dispatcher
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def create_start_kb():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True,
                                   keyboard=[
                                       [
                                           KeyboardButton("Замовити доставку"),
                                           KeyboardButton("Мої доставки")

                                       ],
                                       [
                                           KeyboardButton("Де знаходиться магазин"),
                                           KeyboardButton("Наші контакти")
                                       ]
                                   ])
    return keyboard
