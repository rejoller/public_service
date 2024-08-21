import logging


from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.dialects.postgresql import insert

from database.models import First_layer, Success_clicks

from datetime import datetime as dt


class ClickManager:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def add_success_click(self, user_id: int):
        try:
            add_click_query = (
                insert(Success_clicks)
                .values(user_id=user_id, click_time=dt.now())
                .on_conflict_do_nothing()
            )
            await self.session.execute(add_click_query)
            await self.session.commit()
        except Exception as e:
            logging.info(f"не удалось добавить запись: {e}")

        add_click_query = (
            insert(Success_clicks)
            .values(user_id=user_id, click_time=dt.now())
            .on_conflict_do_nothing()
        )
        await self.session.execute(add_click_query)
        await self.session.commit()

    async def add_first_layer_click(self, user_id: int, callback: str):
        add_callback_query = (
            insert(First_layer)
            .values(user_id=user_id, click_time=dt.now(), callback=callback)
            .on_conflict_do_nothing()
        )
        await self.session.execute(add_callback_query)
        await self.session.commit()
