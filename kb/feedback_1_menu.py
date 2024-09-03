from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


feedback_markup = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Принять участие в конкурсе", callback_data="want_to_participate", url='https://lpd.ranepa.ru/lk/register/136/'
            )
        ],
        [
            InlineKeyboardButton(
                text="Дополнительная информация",
                callback_data="ok_need_additional_info",
            )
        ],
        [
            InlineKeyboardButton(
                text="Вернуться в главное меню", callback_data="main_menu"
            )
        ],
    ]
)
