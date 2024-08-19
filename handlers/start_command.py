from aiogram.filters import CommandStart
from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from sqlalchemy.ext.asyncio import AsyncSession

from config import START_TEXT
from users.user_manager import UserManager

from kb.main_menu import markup

router = Router()




@router.message(CommandStart(), F.chat.type == 'private')
async def handle_start(message: Message, state: FSMContext, session: AsyncSession):
    user_manager = UserManager(session)
    user_data = user_manager.extract_user_data_from_message(message)
    await user_manager.add_user_if_not_exists(user_data)
    await message.answer(START_TEXT, reply_markup=markup)