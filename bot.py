import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.types import FSInputFile

import os
from dotenv import load_dotenv

from emoji import emojize as em

load_dotenv()
logging.basicConfig(level=logging.INFO)

API_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    BG_logo = FSInputFile("images/BG_logo.jpg")

    await message.answer_photo(
        BG_logo,
        caption=em("Привет!:waving_hand:\n\nЯ помогу тебе быстрее отрастить бороду и волосы. Буду напоминать тебе использовать средство и следить за результатами.\n\nВыбери удобное время для напоминаний:")
    )

# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())