from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.types import FSInputFile
from emoji import emojize as em
from keyboards.inline import set_time_inline_kb

start_router = Router()

@start_router.message(Command('start'))
async def cmd_start(message: Message):
    BG_logo = FSInputFile("images/BG_logo.jpg")
    
    await message.answer_photo(
        BG_logo,
        caption=em("Привет!:waving_hand:\n\nЯ помогу тебе быстрее отрастить бороду и волосы. Буду напоминать тебе использовать средство и следить за результатами.\n\nВыбери удобное время для напоминаний:"), reply_markup=set_time_inline_kb())

