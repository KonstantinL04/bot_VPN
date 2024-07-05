from aiogram.types import (InlineKeyboardMarkup, InlineKeyboardButton)
from aiogram.utils.keyboard import InlineKeyboardBuilder
 
main = InlineKeyboardMarkup(inline_keyboard=[
  [InlineKeyboardButton(text='Подключиться',callback_data='subscribe')],
  [InlineKeyboardButton(text='Помощь',callback_data='help')]
 ], 
 resize_keyboard=True,
 input_field_placeholder='Выберите пункт меню. ')

setting = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Google', url='https://google.com')]
])

subscribes = ['Тестовый доступ на 1 день' ,'Доступ на 30 дней', 'Доступ на 90 дней', 'Доступ на 180 дней', 'Главное меню']
async def inline_subscribes():
    keyboard = InlineKeyboardBuilder()
    for subscribe in subscribes:
        keyboard.add(InlineKeyboardButton(text=subscribe, callback_data=f'subscribe_{subscribe}'))
    return keyboard.adjust(1).as_markup()

get_days_1 = ['Получить ключ', 'Назад']
async def inline_subscribe_1_day():
    keyboard = InlineKeyboardBuilder()
    for get_day_one in get_days_1:
        keyboard.add(InlineKeyboardButton(text=get_day_one, callback_data=f'day_{get_day_one}'))
    return keyboard.adjust(1).as_markup()


days_1 = ['Проверить доступ на 1 день', 'Назад']
async def inline_subscribe_check_1_day():
    keyboard = InlineKeyboardBuilder()
    for day_1 in days_1:
        keyboard.add(InlineKeyboardButton(text=day_1, callback_data=f'check_{day_1}'))
    return keyboard.adjust(1).as_markup()

days_30 = ['Проверить доступ на 30 дней', 'Назад']
async def inline_subscribe_check_30_days():
    keyboard = InlineKeyboardBuilder()
    for day_30 in days_30:
        keyboard.add(InlineKeyboardButton(text=day_30, callback_data=f'check_{day_30}'))
    return keyboard.adjust(1).as_markup()

days_90 = ['Проверить доступ на 90 дней', 'Назад']
async def inline_subscribe_check_90_days():
    keyboard = InlineKeyboardBuilder()
    for day_90 in days_90:
        keyboard.add(InlineKeyboardButton(text=day_90, callback_data=f'check_{day_90}'))
    return keyboard.adjust(1).as_markup()

days_180 = ['Проверить доступ на 180 дней', 'Назад']
async def inline_subscribe_check_180_days():
    keyboard = InlineKeyboardBuilder()
    for day_180 in days_180:
        keyboard.add(InlineKeyboardButton(text=day_180, callback_data=f'check_{day_180}'))
    return keyboard.adjust(1).as_markup()


key_days_1 = ['Готово']
async def inline_get_subscribe_1_day():
    keyboard = InlineKeyboardBuilder()
    for key_day_1 in key_days_1:
        keyboard.add(InlineKeyboardButton(text=key_day_1, callback_data=f'key_day_1_{key_day_1}'))
    return keyboard.adjust(1).as_markup()

months_one = ['Оплатить 120₽', 'Назад']
async def inline_pay_subscribe_30_days():
    keyboard = InlineKeyboardBuilder()
    for month_one in months_one:
        keyboard.add(InlineKeyboardButton(text=month_one, callback_data=f'month_{month_one}'))
    return keyboard.adjust(1).as_markup()

months_three = ['Оплатить 320₽', 'Назад']

async def inline_pay_subscribe_90_days():
    keyboard = InlineKeyboardBuilder()
    for subscribe_320r in months_three:
        keyboard.add(InlineKeyboardButton(text=subscribe_320r, callback_data=f'month_{subscribe_320r}'))
    return keyboard.adjust(1).as_markup()

months_six = ['Оплатить 600₽', 'Назад']

async def inline_pay_subscribe_180_days():
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