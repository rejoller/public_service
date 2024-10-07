import logging
from aiogram import F, Router, Bot
from aiogram.types import CallbackQuery
from sqlalchemy.ext.asyncio import AsyncSession

from utils.text_messages  import CONTACTS_AND_MENU_TEXT, CONTACTS_PHOTO
from kb.contacts_and_main_menu import contacts_and_menu_markup


router = Router()

@router.callback_query(F.data == 'ok_need_additional_info')
async def handle_waiting_for_choise(query: CallbackQuery, session: AsyncSession, bot: Bot):

    message_id = query.message.message_id
    if message_id:
        try:
            await bot.delete_message(chat_id=query.message.chat.id, message_id=message_id)
        except Exception as e:
            logging.info(f'не удалось удалить сообщение {e}')
    await query.message.answer_photo(caption=CONTACTS_AND_MENU_TEXT, parse_mode='HTML', reply_markup=contacts_and_menu_markup, photo=CONTACTS_PHOTO)
    await query.answer()