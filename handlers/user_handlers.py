from aiogram import F, Router, types
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery, PreCheckoutQuery, ContentType
from DB.checkUser import get_key
import keyboards.keyboards as kb
from lexicon.lexicon_ru import LEXICON_RU
from services.services import get_user_name
from config import PaysToken, load_pay_token
import os
from scripts.create_ovpn_subscribes import execute_remote_script


payToken: PaysToken = load_pay_token()
PAYMENT_TOKEN: str = payToken.token.token

router = Router()

# Prices
PRICE_1_MONTH = types.LabeledPrice(label="Подписка на 1 месяц", amount=120 * 100)  # 120 руб в копейках
PRICE_3_MONTHS = types.LabeledPrice(label="Подписка на 3 месяца", amount=320 * 100)  # 320 руб в копейках
PRICE_6_MONTHS = types.LabeledPrice(label="Подписка на 6 месяцев", amount=600 * 100)  # 600 руб в копейках

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

@router.callback_query(F.data == 'subscribe_Тестовый доступ на 1 день')
async def subscribe_1_day(callback: CallbackQuery):
    await callback.message.edit_text(LEXICON_RU['subscribe_1_day'], reply_markup=await kb.inline_subscribe_1_day(), parse_mode='HTML')    

@router.callback_query(F.data == 'day_Получить ключ')
async def subscribe_1_day(callback: CallbackQuery):
    username = callback.from_user.username
    if username:
        message, key = get_key(username, 1)
        if key:
            await callback.message.edit_text(message, reply_markup=await kb.inline_get_subscribe_1_day(), parse_mode='HTML')
        elif key:
            await callback.message.edit_text(message, reply_markup=await kb.inline_get_subscribe_1_day(), parse_mode='HTML')
        else:
            ovpn_file_path = execute_remote_script(username, day=1)
            await callback.message.answer_document(types.InputFile(ovpn_file_path))
            await callback.message.edit_text(message, reply_markup=await kb.inline_get_subscribe_1_day() ,parse_mode='HTML')
            os.remove(ovpn_file_path)
    else:
        message = "Не удалось определить ваш никнейм в Telegram."
        await callback.message.edit_text(message, parse_mode='HTML')


@router.callback_query(F.data == 'day_Назад')
async def back_to_subscribe(callback: CallbackQuery):
    await callback.message.edit_text(LEXICON_RU['subscribe'], reply_markup=await kb.inline_subscribes(), parse_mode='HTML')

@router.callback_query(F.data == 'key_day_1_Готово')
async def done_day_1(callback: CallbackQuery):
    await callback.message.edit_text(LEXICON_RU['start'], reply_markup=kb.main, parse_mode='HTML')


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

@router.callback_query(F.data == 'month_Оплатить 120₽')
async def buy_120(callback: CallbackQuery):
    if PAYMENT_TOKEN.split(':')[1] == 'TEST':
        await callback.message.answer("Тестовый платеж!!!")

    await callback.message.answer_invoice(
        title="Подписка на 1 месяц",
        description="Активация подписки на бота на 1 месяц",
        provider_token=PAYMENT_TOKEN,
        currency="rub",
        photo_url="https://i.pcmag.com/imagery/reviews/00JXUu9pun1kRsTQWb6Pvh8-7.fit_lim.size_1050x591.v1569476244.jpg",
        photo_width=400,
        photo_height=200,
        photo_size=1200,
        is_flexible=False,
        prices=[PRICE_1_MONTH],
        start_parameter="one-month-subscription",
        payload="test-invoice-payload-120"
    )

@router.callback_query(F.data == 'month_Оплатить 320₽')
async def buy_320(callback: CallbackQuery):
    if PAYMENT_TOKEN.split(':')[1] == 'TEST':
        await callback.message.answer("Тестовый платеж!!!")

    await callback.message.answer_invoice(
        title="Подписка на 3 месяца",
        description="Активация подписки на бота на 3 месяца",
        provider_token=PAYMENT_TOKEN,
        currency="rub",
        photo_url="https://i.pcmag.com/imagery/reviews/00JXUu9pun1kRsTQWb6Pvh8-7.fit_lim.size_1050x591.v1569476244.jpg",
        photo_width=400,
        photo_height=200,
        photo_size=1200,
        is_flexible=False,
        prices=[PRICE_3_MONTHS],
        start_parameter="three-month-subscription",
        payload="test-invoice-payload-320"
    )

@router.callback_query(F.data == 'month_Оплатить 600₽')
async def buy_600(callback: CallbackQuery):
    if PAYMENT_TOKEN.split(':')[1] == 'TEST':
        await callback.message.answer("Тестовый платеж!!!")

    await callback.message.answer_invoice(
        title="Подписка на 6 месяцев",
        description="Активация подписки на бота на 6 месяцев",
        provider_token=PAYMENT_TOKEN,
        currency="rub",
        photo_url="https://i.pcmag.com/imagery/reviews/00JXUu9pun1kRsTQWb6Pvh8-7.fit_lim.size_1050x591.v1569476244.jpg",
        photo_width=400,
        photo_height=200,
        photo_size=1200,
        is_flexible=False,
        prices=[PRICE_6_MONTHS],
        start_parameter="six-month-subscription",
        payload="test-invoice-payload-600"
    )

#проверка оплаты
@router.pre_checkout_query(lambda query: True)
async def pre_checkout_query(pre_checkout_q: PreCheckoutQuery):
    await pre_checkout_q.bot.answer_pre_checkout_query(pre_checkout_q.id, ok=True)

@router.message(F.content_type == ContentType.SUCCESSFUL_PAYMENT)
async def successful_payment(message: Message):
    print("SUCCESSFUL PAYMENT:")
    payment_info = message.successful_payment.to_python()
    for k, v in payment_info.items():
        print(f"{k} = {v}")

    await message.answer(f"Платеж на сумму {message.successful_payment.total_amount // 100} {message.successful_payment.currency} прошел успешно!!!")

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
