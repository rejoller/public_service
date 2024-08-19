import logging
from aiogram import Bot, types, F, Router
from aiogram.types import CallbackQuery
from sqlalchemy.ext.asyncio import AsyncSession

from config import MAIN_MENU_TEXT
from kb.feedback_1_menu import feedback_markup


router = Router()

@router.callback_query(F.data == 'main_menu')
async def handle_waiting_for_choise(query: types.CallbackQuery, session: AsyncSession, bot: Bot):

    message_id = query.message.message_id
    if message_id:
        try:
            await bot.delete_message(chat_id=query.message.chat.id, message_id=message_id)
            await query.message.answer(text=MAIN_MENU_TEXT, parse_mode='HTML')
        except Exception as e:
            logging.info(f'не удалось удалить сообщение {e}')
            await query.message.answer(text=MAIN_MENU_TEXT, parse_mode='HTML')
    