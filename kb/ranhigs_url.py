from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


markup = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="О конкурсе", url="https://lpd.ranepa.ru/lk/register/136/")],
        
        [InlineKeyboardButton(text='Вернуться в главное меню', callback_data='main_menu')]
    ]
)
