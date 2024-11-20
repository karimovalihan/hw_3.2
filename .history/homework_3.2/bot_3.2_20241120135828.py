import asyncio
from aiogram import Bot, Dispatcher, types, F

from config import token

bot = Bot(token=token)
dp = Dispatcher()


async def main():
    dp.
    await dp.start_polling(bot)

try:
    asyncio.run(main())
except KeyboardInterrupt:
    print("выход")
