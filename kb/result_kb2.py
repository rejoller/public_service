from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


feedback_markup = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Далее", callback_data="result_steps"
            )
        ],
        [
            InlineKeyboardButton(
                text="Назад", callback_data="main_menu"
            )
        ]
        
        ]
)