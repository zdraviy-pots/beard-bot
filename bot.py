import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command

from config import API_TOKEN, DATABASE_URL, admins
from services.sheduler import start_scheduler
from handlers.start import start_router
from handlers.reminders import reminders_router

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

async def main():
    dp.include_router(start_router)
    dp.include_router(reminders_router)

    await start_scheduler()
    
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())