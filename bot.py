import asyncio
import logging
from aiogram import Bot, Dispatcher

from config import API_TOKEN
from services.functions import start_all_users
from services.sheduler import start_scheduler
from handlers.start import start_router
from handlers.choosing import choose_time_router
from handlers.reminders import reminders_router

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

async def main():
    dp.include_router(start_router)
    dp.include_router(choose_time_router)
    dp.include_router(reminders_router)

    await start_scheduler()
    await start_all_users(bot)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())