import logging
from aiogram import F, Router, Bot
from aiogram.types import CallbackQuery
from sqlalchemy.ext.asyncio import AsyncSession


from kb.ranhigs_url import markup
from users.click_manager import ClickManager


router = Router()


@router.callback_query(F.data == "want_to_participate")
async def handle_waiting_for_choise(
    query: CallbackQuery, session: AsyncSession, bot: Bot):
    click_manager = ClickManager(session)
    await click_manager.add_success_click(query.from_user.id)
