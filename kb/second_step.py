from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


feedback_markup = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Далее", callback_data="second_step"
            )
        ]]
)