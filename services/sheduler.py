from datetime import datetime
import os
import shutil
from apscheduler.triggers.cron import CronTrigger 
from apscheduler.schedulers.asyncio import AsyncIOScheduler

scheduler = AsyncIOScheduler(timezone='UTC')

async def add_reminder(job_function, user_id, job_id, reminder_time, bot):
    trigger = CronTrigger(hour=reminder_time.hour, minute=reminder_time.minute, second=0, timezone='UTC')
    scheduler.add_job(job_function, trigger, args=[user_id, bot], id=job_id, replace_existing=True)

async def remove_reminder(user_id):
    scheduler.remove_job(str(user_id)+'_morning')
    scheduler.remove_job(str(user_id)+'_evening')

def create_backup():
    original_db = 'db/beard_bot_DB.db'
    backup_db = f"db/backup.db"
    
    try:
        if os.path.exists(backup_db):
            os.remove(backup_db)
            print(f"Старая резервная копия {backup_db} удалена.")

        shutil.copy(original_db, backup_db)
        print(f"Резервная копия успешно создана: {backup_db}")

    except Exception as e:
        print(f"Ошибка при создании резервной копии: {e}")

async def start_scheduler():
    scheduler.start()
    scheduler.add_job(create_backup, 'interval', days=1, start_date='2025-02-20 00:00:00')