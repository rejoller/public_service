import logging
from aiogram import Bot, F, Router
from aiogram.types import CallbackQuery
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.dialects.postgresql import insert

from utils.text_messages  import RESULTS_TEXT
from database.models import First_layer
from kb.results_kb import results_markup
from datetime import datetime as dt



router = Router()

@router.callback_query(F.data == 'results')
async def handle_waiting_for_choise(query: CallbackQuery, session: AsyncSession, bot: Bot):

    message_id = query.message.message_id
    if message_id:
        try:
            await bot.delete_message(chat_id=query.message.chat.id, message_id=message_id)
            await query.message.answer(text=RESULTS_TEXT, parse_mode='HTML', reply_markup=results_markup)
            add_callback = insert(First_layer).values(
                user_id=query.from_user.id,
                click_time = dt.now(),
                callback = query.data
                
            ).on_conflict_do_nothing()
            await session.execute(add_callback)
            await session.commit()
        except Exception as e:
            logging.info(f'не удалось удалить сообщение {e}')
            await query.message.answer(text=RESULTS_TEXT, parse_mode='HTML', reply_markup=results_markup)
            add_callback = insert(First_layer).values(
                user_id=query.from_user.id,
                click_time = dt.now(),
                callback = query.data
                
            ).on_conflict_do_nothing()
            await session.execute(add_callback)
            await session.commit()
    