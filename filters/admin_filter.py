from aiogram.filters import BaseFilter
from aiogram.types import Message

from config import ADMINS_LIST


class AdminFilter(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        return message.from_user.id in ADMINS_LIST
        



