import logging
from aiogram import Bot, F, Router
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from sqlalchemy.ext.asyncio import AsyncSession

from utils.text_messages  import MAIN_MENU_TEXT
from kb.main_menu import markup


router = Router()

@router.callback_query(F.data == 'main_menu')
async def handle_main_menu(query: CallbackQuery, bot: Bot, state: FSMContext):

    message_id = query.message.message_id
    if message_id:
        try:
            await bot.delete_message(chat_id=query.message.chat.id, message_id=message_id)
            await query.message.answer(text=MAIN_MENU_TEXT, parse_mode='HTML', reply_markup=markup)
            await state.clear()
        except Exception as e:
            logging.info(f'не удалось удалить сообщение {e}')
            await query.message.answer(text=MAIN_MENU_TEXT, parse_mode='HTML', reply_markup=markup)
    