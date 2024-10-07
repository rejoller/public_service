import logging
from aiogram import Bot, F, Router
from aiogram.types import CallbackQuery
from sqlalchemy.ext.asyncio import AsyncSession

from users.click_manager import ClickManager
from utils.text_messages  import CALENDAR_TEXT, CALENDAR_PHOTO
from kb.feedback_1_menu import feedback_markup

router = Router()

@router.callback_query(F.data == 'calendar')
async def handle_waiting_for_choise(query: CallbackQuery, session: AsyncSession, bot: Bot):
    click_manager = ClickManager(session)
    message_id = query.message.message_id
    if message_id:
        try:
            await bot.delete_message(chat_id=query.message.chat.id, message_id=message_id)
        except Exception as e:
            logging.info(f'не удалось удалить сообщение {e}')
    await query.message.answer_photo(parse_mode='HTML', reply_markup=feedback_markup, photo=CALENDAR_PHOTO)
    await click_manager.add_first_layer_click(query.from_user.id, callback=query.data)
    await query.answer()