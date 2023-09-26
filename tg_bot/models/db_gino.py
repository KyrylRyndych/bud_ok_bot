from gino import Gino
import datetime
import sqlalchemy as sa
from sqlalchemy import Column, Integer, String, DateTime
from aiogram import Dispatcher
from typing import List
from tg_bot.config import load_config

db = Gino()
postgresurl = load_config().db.POSTGRES_URI


class BaseModel(db.Model):
    __abstract__ = True

    def __str__(self) -> str:
        model = self.__class__.__name__
        table: sa.Table = sa.inspect(self.__class__)
        primary_key_colums: List[sa.Colomn] = table.columns
        values = {
            column.name: getattr(self, self._column_name_map[column.name])
            for column in primary_key_colums
        }
        values_str = " ".join(f"{name}={value!r}" for name, value in values.items())
        return f"<{model} {values_str}>"


class TimeBaseModel(BaseModel):
    __abstract__ = True

    created_at = Column(DateTime(True), server_default=db.func.now())
    updated_at = Column(DateTime(True),
                        default=datetime.datetime.utcnow,
                        onupdate=datetime.datetime.utcnow,
                        server_default=db.func.now())

    async def on_startup(dispatsher: Dispatcher):
        print("Connect with PostgresSQL")
        await db.set_bind(postgresurl)



