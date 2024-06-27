import asyncio

from aiogram import Bot , Dispatcher
from handlers.user_handlers import router as user_router
from handlers.other_handlers import router as other_router


import logging

from config import TOKEN
from handlers.user_handlers import router


bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)

 

async def main():
    dp.include_router(user_router)
    dp.include_router(other_router)

    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit") 