import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart, Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from config import token

bot = Bot(token=token)
dp = Dispatcher()

direction_keyboard = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='BackEnd'), KeyboardButton(text='FrontEnd'), KeyboardButton(text='Дизайн')]
], one_time_keyboard=True)

keyboards = ReplyKeyboardMarkup(keyboard=direction_keyboard, resize_keyboard=True, one_time_keyboard=True)

buttons = [
    [KeyboardButton(text='О нас'), KeyboardButton(text='Направлений'), KeyboardButton(text='Контакты')]]

keyboard = ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True, one_time_keyboard=True)

@dp.message(CommandStart())
async def start(message: types.Message):
    await message.answer("Здравствуйте",reply_markup=keyboard)

@dp.message(Command('help'))
async def help_command(message: types.Message):
    await message.answer("Чем могу помочь?")

@dp.message(F.text =='О нас')
async def about_us(message: types.Message):
    await message.answer("""Мы создаем экосистему для обучения,
                        работы и творчества IT-специалистов Международная IT-академия Geeks (Гикс) был основан
                        Fullstack-разработчиком Айдаром Бакировым и Android-разработчиком Нургазы Сулаймановым в 2018-ом
                        году в Бишкеке с целью дать возможность каждому человеку, даже без опыта в технологиях, гарантированно
                        освоить IT-профессию. На сегодняшний день более 1200 студентов в возрасте от 12 до 45 лет изучают здесь
                        самые популярные и востребованные IT-профессии. Филиальная сеть образовательного центра представлена в таких городах,
                        как Бишкек, Ош, Ташкент и Кара-Балта.""")
    
direction_keyboard = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Первое'), KeyboardButton(text='Второе'), KeyboardButton(text='Третье')],
    [KeyboardButton(text='Backend'), KeyboardButton(text='Frontend'), KeyboardButton(text='Дизайн')],
], one_time_keyboard=True)

keyboards = ReplyKeyboardMarkup(keyboard=direction_keyboard, resize_keyboard=True, one_time_keyboard=True)

@dp.message(F.text == 'Направлений')
async def directions(message: types.Message):
    await message.answer("Выберите направление",reply_markup=keyboards)

@dp.message(F.text == 'Backend')
async def backend(message: types.Message):
    await message.answer("""Бэкенд-разработчик — это
                           специалист, занимающийся
                           разработкой функциональной части
                           веб-сайта или приложения. Его работа заключается
                           создании серверной части приложения, настройке базы данных
                           и разработке API для взаимодействия с фронтенд-решением
                           Стоимость: 12000  сом в месяц
                           Обучение: 5 месяц.""")

@dp.message(F.text == 'Frontend')
async def frontend(message: types.Message):
    await message.answer("""Frontend-разработчик — это специалист,
                           который занимается разработкой пользовательского интерфейса,
                           то есть той части сайта или приложения, которую видят посетители страницы.
                           Главная задача фронтенд разработчика — перевести готовый дизайн-макет в код так,
                           чтобы все работало правильно
                           Стоимость: 12000 сом
                           Обучение: 5 месяц.""")

@dp.message(F.text == 'Дизайн')
async def design(message: types.Message):
    await message.answer("""Дизайнер — это специалист,
                           который занимается визуальным
                           оформлением реальных и виртуальных объектов.
                           Это общее название профессии, которая включает в себя несколько специализаций
                           Стоимость: 12000 сомов
                           Обучение: 5  месяц.""")

@dp.message(F.text == 'контакты')
async def contact(message: types.Message):
    await message.reply_contact(phone_number='+996999000722', last_name='Исакова', first_name='Кудбухон')

async def main():
    await dp.start_polling(bot)

try:
    asyncio.run(main())
except KeyboardInterrupt:
    print("выход")