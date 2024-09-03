from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


feedback_markup = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Далее", callback_data="third_step"
            )
        ],
        [
            InlineKeyboardButton(
                text="Назад", callback_data="first_step"
            )
        ]
        
        ]
)