import sqlite3

def save_reminder(user_id, reminder_time, timezone):
    # conn = sqlite3.connect('db/beard_bot_DB.db')
    # cursor = conn.cursor()

    # cursor.execute(
    # '''
    #     INSERT OR REPLACE INTO reminders (user_id, reminder_time, timezone)
    #     VALUES (?, ?, ?)
    # ''', 
    # (user_id, reminder_time, timezone))
    
    # conn.commit()
    # conn.close()
    return

def get_reminder(user_id):
    # conn = sqlite3.connect('db/beard_bot_DB.db')
    # cursor = conn.cursor()

    # cursor.execute(
    # '''
    #     SELECT reminder_time, timezone FROM reminders WHERE user_id = ?
    # ''', 
    # (user_id,))

    # reminder = cursor.fetchone()
    # conn.close()
    # return reminder
    return
