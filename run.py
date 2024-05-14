import asyncio

from aiogram import Bot , Dispatcher
from aiogram.filters import CommandStart 
from aiogram.types import Message
import logging

from config import TOKEN


bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)

@dp. message (CommandStart())
async def cmd_start(message: Message):
    await message.answer('Привет!')

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit") 