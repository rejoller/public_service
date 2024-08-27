from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


markup = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Губернаторский управленческий резерв", callback_data="reserve"
            )
        ],
        [
            InlineKeyboardButton(
                text="Положение о конкурсе",
                callback_data="about",
                url="http://kadry24.krskstate.ru/rezerv/komis",
            )
        ],
        [InlineKeyboardButton(text="Критерии участия", callback_data="criteries")],
        [InlineKeyboardButton(text="Этапы отбора", callback_data="steps")],
        [
            InlineKeyboardButton(
                text="Календарный график конкурса", callback_data="calendar"
            )
        ],
        [InlineKeyboardButton(text="Итоги конкурса", callback_data="results")],
        [InlineKeyboardButton(text="Контакты", callback_data="contacts")],
    ]
)
