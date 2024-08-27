import logging
from aiogram import Bot, F, Router
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

from utils.text_messages  import MAIN_MENU_TEXT, MAIN_MENU_PHOTO
from kb.main_menu import markup


router = Router()

@router.callback_query(F.data == 'main_menu')
async def handle_main_menu(query: CallbackQuery, bot: Bot, state: FSMContext):
    await state.clear()
    message_id = query.message.message_id
    if message_id:
        try:
            await bot.delete_message(chat_id=query.message.chat.id, message_id=message_id)
        except Exception as e:
            logging.info(f'не удалось удалить сообщение {e}')
    await query.message.answer_photo(caption=MAIN_MENU_TEXT, parse_mode='HTML', reply_markup=markup, photo=MAIN_MENU_PHOTO)
    