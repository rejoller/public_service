from aiogram.filters import CommandStart
from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from sqlalchemy.ext.asyncio import AsyncSession

from utils.text_messages import START_TEXT, MAIN_MENU_PHOTO
from users.user_manager import UserManager

from kb.main_menu import markup

router = Router()


@router.message(CommandStart(), F.chat.type == "private")
async def handle_start(message: Message, session: AsyncSession, state: FSMContext):
    await state.clear()
    user_manager = UserManager(session)
    user_data = user_manager.extract_user_data_from_message(message)
    await user_manager.add_user_if_not_exists(user_data)
    await message.answer_photo(reply_markup=markup, photo=MAIN_MENU_PHOTO)
