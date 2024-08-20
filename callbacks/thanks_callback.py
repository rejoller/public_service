import logging
from aiogram import F, Router, Bot
from aiogram.types import CallbackQuery
from sqlalchemy.ext.asyncio import AsyncSession

from config import THANKS_TEXT
from kb.contacts_and_main_menu import contacts_and_menu_markup


router = Router()

@router.callback_query(F.data == 'ok_no_interes')
async def handle_waiting_for_choise(query: CallbackQuery, session: AsyncSession, bot: Bot):

    message_id = query.message.message_id
    if message_id:
        try:
            await bot.delete_message(chat_id=query.message.chat.id, message_id=message_id)
            await query.message.answer(text=THANKS_TEXT, parse_mode='HTML')
        except Exception as e:
            logging.info(f'не удалось удалить сообщение {e}')
            await query.message.answer(text=THANKS_TEXT, parse_mode='HTML')