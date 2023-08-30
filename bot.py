import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.fsm_storage.redis import RedisStorage2
from aiogram.contrib.middlewares.environment import EnvironmentMiddleware

from tg_bot.config import load_config
from tg_bot.handleres.start import register_start



logger = logging.getLogger(__name__)


def register_all_middlewares(dp, **kwargs):
    dp.setup_middleware(EnvironmentMiddleware(kwargs))


def register_all_filters(dp):
    pass
def register_all_handlers(dp: Dispatcher):
    register_start(dp)

async def main():
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(levelname)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s %(message)s'
    )
    config = load_config(".env")
    bot = Bot(token=config.tg_bot.token)
    storage = RedisStorage2() if config.tg_bot.use_redis else MemoryStorage()
    dp = Dispatcher(bot, storage=storage)
    bot['config'] = config
    register_all_middlewares(dp)
    register_all_filters(dp)
    register_all_handlers(dp)

    try:
        await dp.skip_updates()
        await dp.start_polling()
    finally:
        await dp.storage.close()
        await dp.storage.wait_closed()
        await bot.session.close()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except(KeyboardInterrupt, SystemExit):
        logger.error("Bot stopped!")
