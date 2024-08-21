from aiogram import types
from aiogram import BaseMiddleware
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Callable, Dict, Any, Awaitable
from aiogram import BaseMiddleware
from aiogram.types import TelegramObject, Message
from icecream import ic

from config import ADMINS_LIST

class AdminFilter(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any]
    ) -> Any:
        if "/support" in event.text:
            user_id = event.from_user.id
            ic(user_id)
            if user_id not in ADMINS_LIST:
                try:
                    await Message.answer("У вас нет доступа к этой команде.")
                except:
                    pass
        result = await handler(event, data)
        print("After handler")
        return result
    
    
    
        
        
                