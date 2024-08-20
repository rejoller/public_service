from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton




results_markup = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(
                 text="Принять участие в конкурсе", callback_data="want_to_participate")],
            [InlineKeyboardButton(
                text="Все понятно. Мне сейчас не интересно", callback_data="ok_no_interes")],
            [InlineKeyboardButton(
                 text="Есть вопросы, нужна дополнительная информация", callback_data="ok_need_additional_info")],
            [InlineKeyboardButton(
                 text="Истории успеха резервистов", callback_data="success_story")],
            [InlineKeyboardButton(
                text="Вернуться в главное меню", callback_data="main_menu")]
            
            ]
        )