from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


contacts_and_menu_markup = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Контакты", callback_data="contacts")],
        [
            InlineKeyboardButton(
                text="Вернуться в главное меню", callback_data="main_menu"
            )
        ],
    ]
)
