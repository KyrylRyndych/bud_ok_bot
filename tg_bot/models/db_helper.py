import asyncio
from sqlalchemy.ext.asyncio import create_async_engine


from sqlalchemy.orm import sessionmaker


from tg_bot.config import load_config


class DatabaseHelper:
    def __int__(self):
        self.engine = create_async_engine(
            url=load_config().db.POSTGRES_URI)

        self.session_factory = sessionmaker(bind=self.engine,
                                            autoflash=False,
                                            autocommit=False,
                                            expire_on_commit=False, )
