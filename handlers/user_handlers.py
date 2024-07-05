from aiogram import F, Router, types
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery, PreCheckoutQuery, ContentType
from aiogram.types.input_file import FSInputFile
from DB.checkUser import get_key, check_key
import keyboards.keyboards as kb
from lexicon.lexicon_ru import LEXICON_RU
from services.services import get_user_name
from config import PaysToken, load_pay_token


payToken: PaysToken = load_pay_token()
PAYMENT_TOKEN: str = payToken.token.token

router = Router()

# Prices
PRICE_1_MONTH = types.LabeledPrice(label="Подписка на 30 дней", amount=120 * 100)  # 120 руб в копейках
PRICE_3_MONTHS = types.LabeledPrice(label="Подписка на 90 дней", amount=320 * 100)  # 320 руб в копейках
PRICE_6_MONTHS = types.LabeledPrice(label="Подписка на 180 дней", amount=600 * 100)  # 600 руб в копейках

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
    await callback.message.edit_text(LEXICON_RU['check_subscribe'].format(user_name=callback.from_user.first_name), reply_markup=await kb.inline_subscribe_check_1_day(), parse_mode='HTML')    

@router.callback_query(F.data == 'subscribe_Доступ на 30 дней')
async def subscribe_30_days(callback: CallbackQuery):
    await callback.message.edit_text(LEXICON_RU['check_subscribe'].format(user_name=callback.from_user.first_name), reply_markup=await kb.inline_subscribe_check_30_days(), parse_mode='HTML')

@router.callback_query(F.data == 'subscribe_Доступ на 90 дней')
async def subscribe_90_days(callback: CallbackQuery):
    await callback.message.edit_text(LEXICON_RU['check_subscribe'].format(user_name=callback.from_user.first_name), reply_markup=await kb.inline_subscribe_check_90_days(), parse_mode='HTML')

@router.callback_query(F.data == 'subscribe_Доступ на 180 дней')
async def subscribe_180_days(callback: CallbackQuery):
    await callback.message.edit_text(LEXICON_RU['check_subscribe'].format(user_name=callback.from_user.first_name), reply_markup=await kb.inline_subscribe_check_180_days(), parse_mode='HTML')

@router.callback_query(F.data == 'subscribe_Главное меню')
async def back_to_main(callback: CallbackQuery):
    await callback.message.edit_text(LEXICON_RU['start'].format(user_name=callback.from_user.first_name), reply_markup=kb.main, parse_mode='HTML')


@router.callback_query(F.data == 'check_Проверить доступ на 1 день')
async def check_subscribe_1_day(callback: CallbackQuery):
    username = callback.from_user.username
    if username:
        message_text, file_path = check_key(username, 1)
        if file_path:
            await callback.message.answer_document(FSInputFile(file_path), caption='Вот ваша активная подписка', reply_markup=await kb.inline_get_subscribe_1_day(), parse_mode='HTML') 
        else:
            await callback.message.edit_text(message_text, reply_markup=await kb.inline_subscribe_1_day(), parse_mode='HTML')
    else:
        message_text = "Не удалось определить ваш никнейм в Telegram."
        await callback.message.edit_text(message_text, parse_mode='HTML')    
  

@router.callback_query(F.data == 'check_Проверить доступ на 30 дней')
async def check_subscribe_30_days(callback: CallbackQuery):
    username = callback.from_user.username
    if username:
        message_text, file_path = check_key(username, 30)
        if file_path:
            await callback.message.answer_document(FSInputFile(file_path), caption='Вот ваша активная подписка', reply_markup=await kb.inline_get_subscribe_1_day(), parse_mode='HTML') 
        else:
            await callback.message.edit_text(message_text, reply_markup=await kb.inline_pay_subscribe_30_days(), parse_mode='HTML')
    else:
        message_text = "Не удалось определить ваш никнейм в Telegram."
        await callback.message.edit_text(message_text, parse_mode='HTML')

@router.callback_query(F.data == 'check_Проверить доступ на 90 дней')
async def check_subscribe_90_days(callback: CallbackQuery):
    username = callback.from_user.username
    if username:
        message_text, file_path = check_key(username, 90)
        if file_path:
            await callback.message.answer_document(FSInputFile(file_path), caption='Вот ваша активная подписка', reply_markup=await kb.inline_get_subscribe_1_day(), parse_mode='HTML') 
        else:
            await callback.message.edit_text(message_text, reply_markup=await kb.inline_pay_subscribe_90_days(), parse_mode='HTML')
    else:
        message_text = "Не удалось определить ваш никнейм в Telegram."
        await callback.message.edit_text(message_text, parse_mode='HTML')

@router.callback_query(F.data == 'check_Проверить доступ на 180 дней')
async def check_subscribe_180_days(callback: CallbackQuery):
    username = callback.from_user.username
    if username:
        message_text, file_path = check_key(username, 180)
        if file_path:
            await callback.message.answer_document(FSInputFile(file_path), caption='Вот ваша активная подписка', reply_markup=await kb.inline_get_subscribe_1_day(), parse_mode='HTML') 
        else:
            await callback.message.edit_text(message_text, reply_markup=await kb.inline_pay_subscribe_180_days(), parse_mode='HTML')
    else:
        message_text = "Не удалось определить ваш никнейм в Telegram."
        await callback.message.edit_text(message_text, parse_mode='HTML')

@router.callback_query(F.data == 'check_Назад')
async def back_to_subscribe(callback: CallbackQuery):
    await callback.message.edit_text(LEXICON_RU['subscribe'], reply_markup=await kb.inline_subscribes(), parse_mode='HTML')

@router.callback_query(F.data == 'day_Получить ключ')
async def subscribe_1_day(callback: CallbackQuery):
    username = callback.from_user.username
    if username:
        message, file_path = get_key(username, 1)
        if file_path:
            # Отправляем файл .ovpn пользователю
            await callback.message.answer_document(FSInputFile(file_path), caption="Вот ваш сформированный файл.") 
        else:
            await callback.message.edit_text(message, reply_markup=await kb.inline_get_subscribe_1_day(), parse_mode='HTML')
    else:
        message = "Не удалось определить ваш никнейм в Telegram."
        await callback.message.edit_text(message, parse_mode='HTML')
    
@router.callback_query(F.data == 'month_Оплатить 120₽')
async def buy_120(callback: CallbackQuery):
    if PAYMENT_TOKEN.split(':')[1] == 'TEST':
        await callback.message.answer("Тестовый платеж!!!")

    await callback.message.answer_invoice(
        title="Доступ на 30 дней",
        description="Активация доступа для OpenVPN на 30 дней.",
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
        title="Доступ на 90 дней",
        description="Активация доступа для OpenVPN на 90 дней.",
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
        title="Доступ на 180 дней",
        description="Активация доступа для OpenVPN на 180 дней.",
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

@router.callback_query(F.data == 'day_Назад')
async def back_to_subscribe(callback: CallbackQuery):
    await callback.message.edit_text(LEXICON_RU['subscribe'], reply_markup=await kb.inline_subscribes(), parse_mode='HTML')

@router.callback_query(F.data == 'key_day_1_Готово')
async def done_day_1(callback: CallbackQuery):
    await callback.message.edit_text(LEXICON_RU['start'], reply_markup=kb.main, parse_mode='HTML')

@router.callback_query(F.data == 'month_Назад')
async def back_to_subscribe(callback: CallbackQuery):
    await callback.message.edit_text(LEXICON_RU['subscribe'], reply_markup=await kb.inline_subscribes(), parse_mode='HTML')


#проверка оплаты
@router.pre_checkout_query(lambda query: True)
async def pre_checkout_query(pre_checkout_q: PreCheckoutQuery):
    await pre_checkout_q.bot.answer_pre_checkout_query(pre_checkout_q.id, ok=True)

# Обработка успешного платежа
@router.message(F.successful_payment)
async def successful_payment_handler(message: Message):
    print("SUCCESSFUL PAYMENT:")
    payment_info = message.successful_payment
    
    # Определение типа подписки и отправка соответствующего файла .ovpn
    if payment_info.invoice_payload == "test-invoice-payload-120":
        username = message.from_user.username
        if username:
            message_text, file_path = get_key(username, 30)
            if file_path:
                await message.answer_document(FSInputFile(file_path), caption="Благодарим за покупку!\n\n Вот ваш сформированный файл:" ,reply_markup=await kb.inline_get_subscribe_1_day()) 
            else:
                await message.answer(message_text, reply_markup=await kb.inline_get_subscribe_1_day(), parse_mode='HTML')
        else:
            message_text = "Не удалось определить ваш никнейм в Telegram."
            await message.answer(message_text, parse_mode='HTML')
    
    elif payment_info.invoice_payload == "test-invoice-payload-320":
        username = message.from_user.username
        if username:
            message_text, file_path = get_key(username, 90)
            if file_path:
                await message.answer_document(FSInputFile(file_path), caption="Благодарим за покупку!\n\n Вот ваш сформированный файл: ваш сформированный файл.",reply_markup=await kb.inline_get_subscribe_1_day()) 
            else:
                await message.answer(message_text, reply_markup=await kb.inline_get_subscribe_1_day(), parse_mode='HTML')
        else:
            message_text = "Не удалось определить ваш никнейм в Telegram."
            await message.answer(message_text, parse_mode='HTML')
    
    elif payment_info.invoice_payload == "test-invoice-payload-600":
        username = message.from_user.username
        if username:
            message_text, file_path = get_key(username, 180)
            if file_path:
                await message.answer_document(FSInputFile(file_path), caption="Вот Благодарим за покупку!\n\n Вот ваш сформированный файл: сформированный файл.",reply_markup=await kb.inline_get_subscribe_1_day()) 
            else:
                await message.answer(message_text, reply_markup=await kb.inline_get_subscribe_1_day(), parse_mode='HTML')
        else:
            message_text = "Не удалось определить ваш никнейм в Telegram."
            await message.answer(message_text, parse_mode='HTML')

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
