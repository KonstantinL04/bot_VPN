from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
 
main = InlineKeyboardMarkup(inline_keyboard=[
  [InlineKeyboardButton(text='Подключиться',callback_data='subscribe')],
  [InlineKeyboardButton(text='Помощь',callback_data='help')]
 ], 
 resize_keyboard=True,
 input_field_placeholder='Выберите пункт меню. ')

setting = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Google', url='https://google.com')]
])

subscribes = ['Тестовый доступ на 1 день' ,'1 месяц – 120₽', '3 месяца – 320₽', '6 месяцев – 600₽', 'Главное меню']

async def inline_subscribes():
    keyboard = InlineKeyboardBuilder()
    for subscribe in subscribes:
        keyboard.add(InlineKeyboardButton(text=subscribe, callback_data=f'subscribe_{subscribe}'))
    return keyboard.adjust(1).as_markup()


months_one = ['Оплатить 120₽', 'Проверить оплату', 'Назад']

async def inline_subscribe_1month():
    keyboard = InlineKeyboardBuilder()
    for month_one in months_one:
        keyboard.add(InlineKeyboardButton(text=month_one, callback_data=f'month_{month_one}'))
    return keyboard.adjust(1).as_markup()

months_three = ['Оплатить 320₽', 'Проверить оплату', 'Назад']

async def inline_subscribe_3month():
    keyboard = InlineKeyboardBuilder()
    for subscribe_320r in months_three:
        keyboard.add(InlineKeyboardButton(text=subscribe_320r, callback_data=f'month_{subscribe_320r}'))
    return keyboard.adjust(1).as_markup()

months_six = ['Оплатить 600₽', 'Проверить оплату', 'Назад']

async def inline_subscribe_6month():
    keyboard = InlineKeyboardBuilder()
    for subscribe_600r in months_six:
        keyboard.add(InlineKeyboardButton(text=subscribe_600r, callback_data=f'month_{subscribe_600r}'))
    return keyboard.adjust(1).as_markup()

helps = ['Как подключиться?', 'Не работает VPN', 'Главное меню']

async def inline_help():
    keyboard = InlineKeyboardBuilder()
    for help in helps:
        keyboard.add(InlineKeyboardButton(text=help, callback_data=f'help_{help}'))
    return keyboard.adjust(1).as_markup()

helps_phone = ['iOS', 'Android', 'Назад']

async def inline_help_phone():
    keyboard = InlineKeyboardBuilder()
    for phone in helps_phone:
        keyboard.add(InlineKeyboardButton(text=phone, callback_data=f'phone_{phone}'))
    return keyboard.adjust(1).as_markup()

helps_phone_downloads = ['Готово!', 'Назад']

async def inline_help_phone_download():
    keyboard = InlineKeyboardBuilder()
    for download in helps_phone_downloads:
        keyboard.add(InlineKeyboardButton(text=download, callback_data=f'download_{download}'))
    return keyboard.adjust(1).as_markup()

helps_phone_downloads_done = ['Главное меню']

async def inline_help_phone_download_done():
    keyboard = InlineKeyboardBuilder()
    for done in helps_phone_downloads_done:
        keyboard.add(InlineKeyboardButton(text=done, callback_data=f'done_{done}'))
    return keyboard.adjust(1).as_markup()