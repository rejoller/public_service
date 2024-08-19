from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton




feedback_markup = InlineKeyboardMarkup(inline_keyboard=[
            [
            InlineKeyboardButton(
                text="Все понятно. Мне сейчас не интересно", callback_data="ok_no_interes")],
            [InlineKeyboardButton(
                 text="Есть вопросы, нужна дополнительная информация", callback_data="ok_need_additional_info")],
            [InlineKeyboardButton(
                 text="Хочу участвовать", callback_data="want_to_participate")],
            [InlineKeyboardButton(
                text="Вернуться в главное меню", callback_data="main_menu")]
            ]
        )
  