import asyncio
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.redis import RedisStorage

from config import BOT_TOKEN, REDIS_URL
from logger.logging_config import setup_logging
from logger.logging_middleware import LoggingMiddleware

from handlers import setup_routers

from database.db import DataBaseSession
from database.engine import create_db, session_maker, drop_db


storage = RedisStorage.from_url(REDIS_URL)



async def main():
    setup_logging()


    bot = Bot(BOT_TOKEN)
    dp = Dispatcher(storage=storage)
    dp.update.middleware(DataBaseSession(session_pool=session_maker))
    dp.message.middleware(LoggingMiddleware())

    router = setup_routers()
    dp.include_router(router)
    await create_db()
    print('Бот запущен и готов к приему сообщений')
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types(), skip_updates=True)
    

if __name__ == "__main__":
    asyncio.run(main())