from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton




markup = InlineKeyboardMarkup(inline_keyboard=[
            [
            InlineKeyboardButton(
                text="О конкурсе", callback_data="about")],
            [InlineKeyboardButton(
                 text="Критерии для участников", callback_data="criteries")],
            [InlineKeyboardButton(
                 text="Этапы отбора", callback_data="steps")],
            [InlineKeyboardButton(
                text="Календарный график конкурса", callback_data="calendar")],
            [InlineKeyboardButton(
                text="Что получают резервисты", callback_data="what_can_get")]
            ]
        )