from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from aiogram.types import FSInputFile
from aiogram import Bot
from datetime import datetime
import pytz

from keyboards.inline import get_serum_inline_kb
from db_handlers.functions import save_reminder, get_reminder
from services.sheduler import add_reminder

reminders_router = Router()

@reminders_router.callback_query(lambda c: c.data in ['morning'])
async def set_time(call: CallbackQuery, bot: Bot):
    user_id = call.from_user.id
    reminder_time = '10:00'

    # if call.data == 'morning':
    #     reminder_time = "08:00"  
    # elif call.data == 'evening':
    #     reminder_time = "20:00"  

    user_timezone = pytz.timezone('Europe/Moscow') 
    reminder_time_utc = datetime.strptime(reminder_time, "%H:%M")
    reminder_time_utc = user_timezone.localize(reminder_time_utc)

    save_reminder(user_id, reminder_time, str(user_timezone))
    await add_reminder(send_reminder, user_id, reminder_time_utc, bot)

    await call.answer(f'Напоминание установлено на {reminder_time}')

async def send_reminder(user_id, bot: Bot):
    await bot.send_message(user_id, text="Пора применить средство для роста бороды!", reply_markup=get_serum_inline_kb(user_id))

@reminders_router.callback_query(lambda c: c.data.startswith('used_'))
async def serum_used(call: CallbackQuery):
    user_id = call.from_user.id

    await call.answer()
    await call.message.delete()


