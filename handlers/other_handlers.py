from aiogram import Router
from aiogram.types import Message

router = Router()

@router.message()
async def handle_unexpected_message(message: Message):
    await message.reply("Извините, я не понял ваше сообщение. Попробуйте выбрать пункт меню.")
