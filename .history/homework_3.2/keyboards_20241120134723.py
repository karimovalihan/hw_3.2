from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from config import token

buttons = [
    [KeyboardButton(text='О нас'), KeyboardButton(text='Направлений'), KeyboardButton(text='Контакты')]
]

direction_keyboard = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Backend'), KeyboardButton(text='Frontend'), KeyboardButton(text='Дизайн')],
    [KeyboardButton(text='Назад')] 
], one_time_keyboard=True)

keyboard = ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True, one_time_keyboard=True)

keyboards = ReplyKeyboardMarkup(keyboard=direction_keyboard.keyboard, resize_keyboard=True, one_time_keyboard=True)