from aiogram.filters import CommandStart, Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from config import token, types

from keyboards import *

@dp.message(CommandStart())
async def start(message: types.Message):
    await message.answer("Здравствуйте", reply_markup=keyboard)

@dp.message(Command('help'))
async def help_command(message: types.Message):
    await message.answer("Чем могу помочь?")

@dp.message(F.text == 'О нас')
async def about_us(message: types.Message):
    await message.answer("""Мы создаем экосистему для обучения,
                        работы и творчества IT-специалистов. Международная IT-академия Geeks (Гикс) была основана
                        Fullstack-разработчиком Айдаром Бакировым и Android-разработчиком Нургазы Сулаймановым в 2018-ом
                        году в Бишкеке с целью дать возможность каждому человеку, даже без опыта в технологиях, гарантированно
                        освоить IT-профессию. На сегодняшний день более 1200 студентов в возрасте от 12 до 45 лет изучают здесь
                        самые популярные и востребованные IT-профессии. Филиальная сеть образовательного центра представлена в таких городах,
                        как Бишкек, Ош, Ташкент и Кара-Балта.""", reply_markup=keyboard)

@dp.message(F.text == 'Направлений')
async def directions(message: types.Message):
    await message.answer("Выберите направление", reply_markup=direction_keyboard)

@dp.message(F.text == 'Backend')
async def backend(message: types.Message):
    await message.answer("""Бэкенд-разработчик — это специалист, занимающийся разработкой функциональной части
                           веб-сайта или приложения. Его работа заключается в создании серверной части приложения, настройке базы данных
                           и разработке API для взаимодействия с фронтенд-решением.
                           Стоимость: 12000 сом в месяц.
                           Обучение: 5 месяцев.""", reply_markup=direction_keyboard)

@dp.message(F.text == 'Frontend')
async def frontend(message: types.Message):
    await message.answer("""Frontend-разработчик — это специалист, который занимается разработкой пользовательского интерфейса,
                           то есть той части сайта или приложения, которую видят посетители страницы.
                           Главная задача фронтенд-разработчика — перевести готовый дизайн-макет в код так,
                           чтобы все работало правильно.
                           Стоимость: 12000 сом.
                           Обучение: 5 месяцев.""", reply_markup=direction_keyboard)
    
    
@dp.message(F.text == 'Дизайн')
async def design(message: types.Message):
    await message.answer("""Дизайнер — это специалист, который занимается визуальным оформлением реальных и виртуальных объектов.
                           Это общее название профессии, которая включает в себя несколько специализаций.
                           Стоимость: 12000 сомов.
                           Обучение: 5 месяцев.""", reply_markup=direction_keyboard)

@dp.message(F.text == 'Контакты')
async def contact(message: types.Message):
    await message.reply_contact(phone_number='+996999000722', last_name='Исакова', first_name='Кудбухон', reply_markup=keyboard)

@dp.message(F.text == 'Назад')
async def go_back(message: types.Message):
    await message.answer("Вы вернулись в главное меню", reply_markup=keyboard)
    
@dp.message()
async def echo(message: types.message):
    await message.answer("я вас не понял")