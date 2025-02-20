import pytz
from datetime import datetime, timedelta
from emoji import emojize as em

from db_handlers.for_filters import get_user_offset
from db_handlers.main_functions import get_user, get_users
from handlers.reminders import send_reminder
from services.sheduler import add_reminder

def convert_time_to_utc(reminder_time, user_id):
    offset_utc = get_user_offset(user_id)
    hours = int(offset_utc[1:])

    time_delta = timedelta(hours=hours) 

    user_time = datetime.strptime(reminder_time, "%H:%M")
    user_time = user_time - time_delta
    user_time = pytz.utc.localize(user_time)

    return user_time

async def start_all_users(bot):
    for user in get_users():
        user_id = user[0]
        times = [[user[1], 'morning'], [user[2], 'evening']]
        for time in times:
            if time[0] == 'нет' or time[0] == None:
                pass
            else:
                job_id=str(user_id)+'_'+time[1]
                utc_time = convert_time_to_utc(time[0], user_id)
                await add_reminder(send_reminder, user_id, job_id, utc_time, bot)

async def start_user(user_id, bot):
        user = get_user(user_id)
        times = [[user[1], 'morning'], [user[2], 'evening']]
        for time in times:
            if time[0] == 'нет' or time[0] == None:
                pass
            else:
                job_id=str(user_id)+'_'+time[1]
                utc_time = convert_time_to_utc(time[0], user_id)
                await add_reminder(send_reminder, user_id, job_id, utc_time, bot)
                
def generate_caption_choosing(data, time):
    caption=f"Выберите точное время для {('утра' if data == 'morning' else 'вечера')}:\n({time})"
    return caption

def generate_menu_caption(user_id):
    user = get_user(user_id)
    caption = em(f'Время для напоминаний:\n  Утро - {user[1]}\n  Вечер - {user[2]}\n\n:globe_with_meridians: {user[6]} ({user[7]})')
    return caption

def get_selected_timezone(user_id):
    user = get_user(user_id)
    return user[4]
