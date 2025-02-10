from apscheduler.triggers.cron import CronTrigger
from apscheduler.triggers.interval import IntervalTrigger  
from apscheduler.schedulers.asyncio import AsyncIOScheduler

scheduler = AsyncIOScheduler(timezone='Europe/Moscow')

async def add_reminder(job_function, user_id, reminder_time, bot):
    print(user_id, job_function, bot, reminder_time)
    # trigger = CronTrigger(hour=reminder_time.hour, minute=reminder_time.minute, second=0)
    trigger = IntervalTrigger(seconds=10)
    scheduler.add_job(job_function, trigger, args=[user_id, bot], id=str(user_id), replace_existing=True)

async def start_scheduler():
    scheduler.start()

