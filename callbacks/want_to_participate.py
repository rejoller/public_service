import logging
from aiogram import F, Router, Bot
from aiogram.types import CallbackQuery
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.dialects.postgresql import insert


from database.models import Success_clicks
from kb.ranhigs_url import markup
from datetime import datetime as dt


router = Router()

@router.callback_query(F.data == 'want_to_participate')
async def handle_waiting_for_choise(query: CallbackQuery, session: AsyncSession, bot: Bot):

    message_id = query.message.message_id
    if message_id:
        try:
            await bot.delete_message(chat_id=query.message.chat.id, message_id=message_id)
            await query.message.answer(text="Ссылка на сайт", parse_mode='HTML', reply_markup=markup)
            add_callback = insert(Success_clicks).values(
                user_id=query.from_user.id,
                click_time = dt.now()
                
            ).on_conflict_do_nothing()
            await session.execute(add_callback)
            await session.commit()
        except Exception as e:
            logging.info(f'не удалось удалить сообщение {e}')
            await query.message.answer(text="Ссылка на сайт", parse_mode='HTML', reply_markup=markup)
            add_callback = insert(Success_clicks).values(
                user_id=query.from_user.id,
                click_time = dt.now()
                
            ).on_conflict_do_nothing()
            await session.execute(add_callback)
            await session.commit()