import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import logging


from BOT.handlers.metrics import metrics_handler
from config.setting import Setting


logging.basicConfig(level=logging.INFO)


async def on_startup(bot: Bot):
    logging.info("Bot started")


async def on_shutdown(bot: Bot):
    logging.info("Bot stopped")


async def main():
    bot = Bot(token=Setting.BOT_TOKEN)
    dp = Dispatcher()    
    dp.message.register(metrics_handler, Command("metrics"))
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)
    
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(main())