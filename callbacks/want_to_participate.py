import logging
from aiogram import types, F, Router, Bot
from aiogram.types import CallbackQuery
from sqlalchemy.ext.asyncio import AsyncSession

from config import THANKS_TEXT
from kb.ranhigs_url import markup


router = Router()

@router.callback_query(F.data == 'want_to_participate')
async def handle_waiting_for_choise(query: types.CallbackQuery, session: AsyncSession, bot: Bot):

    message_id = query.message.message_id
    if message_id:
        try:
            await bot.delete_message(chat_id=query.message.chat.id, message_id=message_id)
            await query.message.answer(text="Ссылка на сайт", parse_mode='HTML', reply_markup=markup)
        except Exception as e:
            logging.info(f'не удалось удалить сообщение {e}')
            await query.message.answer(text="Ссылка на сайт", parse_mode='HTML', reply_markup=markup)