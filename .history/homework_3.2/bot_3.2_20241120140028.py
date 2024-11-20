import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F

from config import token

bot = Bot(token=token)
dp = Dispatcher()


async def main():
    dp.include_routers(router)
    await dp.start_polling(bot)
    logging.basicConfig(level="INFO")

try:
    asyncio.run(main())
except KeyboardInterrupt:
    print("выход")
