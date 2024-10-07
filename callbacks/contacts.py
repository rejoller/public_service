import logging
from aiogram import Bot, F, Router
from aiogram.types import CallbackQuery
from sqlalchemy.ext.asyncio import AsyncSession

from utils.text_messages  import CONTACTS_PHOTO
from kb.go_back import markup



router = Router()

@router.callback_query(F.data == 'contacts')
async def handle_waiting_for_choise(query: CallbackQuery, session: AsyncSession, bot: Bot):

    message_id = query.message.message_id
    if message_id:
        try:
            await bot.delete_message(chat_id=query.message.chat.id, message_id=message_id) 
        except Exception as e:
            logging.info(f'не удалось удалить сообщение {e}')
        
    await query.message.answer_photo(parse_mode='HTML', photo=CONTACTS_PHOTO, reply_markup=markup)
    await query.answer()
    