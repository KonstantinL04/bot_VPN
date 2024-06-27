from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
import keyboards.keyboards as kb
from lexicon.lexicon_ru import LEXICON_RU
from services.services import get_user_name

router = Router()

# Главное меню
@router.message(CommandStart())
async def cmd_start(message: Message):
    user_name = get_user_name(message)
    await message.reply(LEXICON_RU['start'].format(user_name=user_name),
                        reply_markup=kb.main, parse_mode='HTML')

# Меню выбора тарифа в подключении
@router.callback_query(F.data == 'subscribe')
async def subscribes(callback: CallbackQuery):
    await callback.message.edit_text(LEXICON_RU['subscribe'], reply_markup=await kb.inline_subscribes(), parse_mode='HTML')

@router.callback_query(F.data == 'subscribe_1 месяц – 120₽')
async def subscribe_120(callback: CallbackQuery):
    await callback.message.edit_text(LEXICON_RU['subscribe_120'], reply_markup=await kb.inline_subscribe_1month(), parse_mode='HTML')

@router.callback_query(F.data == 'subscribe_3 месяца – 320₽')
async def subscribe_320(callback: CallbackQuery):
    await callback.message.edit_text(LEXICON_RU['subscribe_320'], reply_markup=await kb.inline_subscribe_3month(), parse_mode='HTML')

@router.callback_query(F.data == 'subscribe_6 месяцев – 600₽')
async def subscribe_600(callback: CallbackQuery):
    await callback.message.edit_text(LEXICON_RU['subscribe_600'], reply_markup=await kb.inline_subscribe_6month(), parse_mode='HTML')

@router.callback_query(F.data == 'subscribe_Главное меню')
async def back_to_main(callback: CallbackQuery):
    await callback.message.edit_text(LEXICON_RU['start'].format(user_name=callback.from_user.first_name), reply_markup=kb.main, parse_mode='HTML')

@router.callback_query(F.data == 'month_Проверить оплату')
async def check_pay(callback: CallbackQuery):
    await callback.message.edit_text(LEXICON_RU['check_pay'].format(user_name=callback.from_user.first_name), reply_markup=await kb.inline_help_phone(), parse_mode='HTML')

@router.callback_query(F.data == 'month_Назад')
async def back_to_subscribe(callback: CallbackQuery):
    await callback.message.edit_text(LEXICON_RU['subscribe'], reply_markup=await kb.inline_subscribes(), parse_mode='HTML')

# Меню выбора помощи
@router.callback_query(F.data == 'help')
async def help(callback: CallbackQuery):
    await callback.message.edit_text(LEXICON_RU['help'].format(user_name=callback.from_user.first_name), reply_markup=await kb.inline_help(), parse_mode='HTML')

@router.callback_query(F.data == 'help_Как подключиться?')
async def help_phone(callback: CallbackQuery):
    await callback.message.edit_text(LEXICON_RU['help_phone'], reply_markup=await kb.inline_help_phone(), parse_mode='HTML')

@router.callback_query(F.data == 'phone_Назад')
async def back_to_help(callback: CallbackQuery):
    await callback.message.edit_text(LEXICON_RU['help'].format(user_name=callback.from_user.first_name), reply_markup=await kb.inline_help(), parse_mode='HTML')

@router.callback_query(F.data == 'help_Главное меню')
async def back_to_main_from_help(callback: CallbackQuery):
    await callback.message.edit_text(LEXICON_RU['start'].format(user_name=callback.from_user.first_name), reply_markup=kb.main, parse_mode='HTML')

# Меню выбора в помощи телефона 
@router.callback_query(F.data == 'phone_iOS')
async def help_phone_iOS(callback: CallbackQuery):
    await callback.message.edit_text(LEXICON_RU['help_phone_ios'], reply_markup=await kb.inline_help_phone_download(), parse_mode='HTML')

@router.callback_query(F.data == 'phone_Android')
async def help_phone_android(callback: CallbackQuery):
    await callback.message.edit_text(LEXICON_RU['help_phone_android'], reply_markup=await kb.inline_help_phone_download(), parse_mode='HTML')

@router.callback_query(F.data == 'download_Назад')
async def back_to_phone(callback: CallbackQuery):
    await callback.message.edit_text(LEXICON_RU['help_phone'], reply_markup=await kb.inline_help_phone(), parse_mode='HTML')

@router.callback_query(F.data == 'download_Готово!')
async def help_phone_download_done(callback: CallbackQuery):
    await callback.message.edit_text(LEXICON_RU['help_phone_download_done'], reply_markup=await kb.inline_help_phone_download_done(), parse_mode='HTML')

@router.callback_query(F.data == 'done_Главное меню')
async def back_to_main2(callback: CallbackQuery):
    await callback.message.edit_text(LEXICON_RU['start'].format(user_name=callback.from_user.first_name), reply_markup=kb.main, parse_mode='HTML')

@router.callback_query(F.data == 'help_Не работает VPN')
async def help_workVPN(callback: CallbackQuery):
    await callback.message.edit_text(LEXICON_RU['help_workVPN'].format(user_name=callback.from_user.first_name), reply_markup=await kb.inline_help_phone_download_done(), parse_mode='HTML')

@router.callback_query(F.data == 'workVPN_Главное меню')
async def back_to_main3(callback: CallbackQuery):
    await callback.message.edit_text(LEXICON_RU['start'].format(user_name=callback.from_user.first_name), reply_markup=kb.main, parse_mode='HTML')
