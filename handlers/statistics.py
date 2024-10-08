from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, FSInputFile
from aiogram.fsm.context import FSMContext

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from database.models import First_layer, Success_clicks, Users

import pandas as pd

from filters.admin_filter import AdminFilter


router = Router()


@router.message(Command("statistics"), F.chat.type == "private", AdminFilter())
async def handle_statistics(message: Message, state: FSMContext, session: AsyncSession):
    stats_query = select(
        Users.user_id,
        Users.first_name,
        Users.last_name,
        Users.username,
        Users.joined_at,
    )
    first_layer_query = (
        select(
            Users.first_name,
            Users.last_name,
            First_layer.callback,
            First_layer.click_time,
        )
        .join(Users, Users.user_id == First_layer.user_id)
        .order_by(First_layer.click_time)
    )




    result_1 = await session.execute(first_layer_query)
    result_1 = result_1.all()
    df_1 = pd.DataFrame(result_1)
    df_1["click_time"] = pd.to_datetime(
        df_1["click_time"], dayfirst=True, format="%d.%m.%Y %H:%M:%S"
    )
    df_1["click_time"] = df_1["click_time"].dt.strftime("%d.%m.%Y %H:%M:%S")
    df_1 = df_1.rename(
        columns={
            "first_name": "Имя",
            "last_name": "Фамилия",
            "callback": "Название кнопки",
            "click_time": "Время клика",
        }
    )

    result = await session.execute(stats_query)
    result = result.all()
    df = pd.DataFrame(result)
    df["joined_at"] = pd.to_datetime(
        df["joined_at"], dayfirst=True, format="%d.%m.%Y %H:%M:%S"
    )
    df["joined_at"] = df["joined_at"].dt.strftime("%d.%m.%Y %H:%M:%S")
    df = df.rename(
        columns={
            "user_id": "ID в Телеграм",
            "first_name": "Имя",
            "last_name": "Фамилия",
            "username": "Никнейм",
            "joined_at": "Дата первого захода в бот",
        }
    )
    df = df.rename(
        columns={
            "first_name": "Имя",
            "last_name": "Фамилия",
            "callback": "Название кнопки",
            "click_time": "Время клика",
        }
    )
    number_of_users = len(df)

    writer = pd.ExcelWriter("Статистика.xlsx", engine="xlsxwriter")

    df.to_excel(writer, index=False, sheet_name="Пользователи")
    worksheet = writer.sheets["Пользователи"]
    for i, col in enumerate(df.columns):
        width = max(df[col].apply(lambda x: len(str(x))).max(), len(col)) + 2
        worksheet.set_column(i, i, width)

    df_1.to_excel(writer, index=False, sheet_name="Первый слой меню")
    worksheet = writer.sheets["Первый слой меню"]
    for i, col in enumerate(df_1.columns):
        width = max(df_1[col].apply(lambda x: len(str(x))).max(), len(col)) + 2
        worksheet.set_column(i, i, width)



    writer.close()

    caption = f"Количество пользователей бота: <b>{number_of_users}</b>\n"

    await message.answer_document(
        document=FSInputFile("Статистика.xlsx"), caption=caption, parse_mode="HTML"
    )

@router.message(Command("statistics"), F.chat.type == "private", ~AdminFilter())
async def handle_not_allowed_to_statistics(message: Message):
    await message.answer("У вас нет прав на просмотр статистики")