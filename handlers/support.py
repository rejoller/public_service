from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.fsm.context import FSMContext
from aiogram.utils.keyboard import InlineKeyboardBuilder


from users.user_states import Form
from config import SUPPORT_IMG

router = Router()


@router.message(Command("support"), F.chat.type == "private")
async def handle_cancel_all_subscriptions(message: Message, state: FSMContext):
    await state.set_state(Form.support)
    builder = InlineKeyboardBuilder()

    markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="В главное меню", callback_data="main_menu")]
        ]
    )

    builder.adjust(1)
    builder.attach(InlineKeyboardBuilder.from_markup(markup))
    caption = (
        "Напишите свое сообщение в техническую поддержку или вернитесь в главное меню"
    )

    await message.answer_photo(photo=SUPPORT_IMG, caption=caption, reply_markup=markup)
