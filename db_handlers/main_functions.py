import sqlite3

def save_user(user_id):
    conn = sqlite3.connect('db/beard_bot_DB.db')
    cursor = conn.cursor()

    cursor.execute(
    f'''
        INSERT OR IGNORE INTO users (user_id, first_time_save, timezone_id)
        VALUES (?, "not yet", 5)
    ''', 
    (user_id,))
    
    conn.commit()
    conn.close()
    return

def save_timezone(user_id, timezone_id):
    conn = sqlite3.connect('db/beard_bot_DB.db')
    cursor = conn.cursor()

    cursor.execute(
    f'''
        UPDATE users 
        SET timezone_id = ?
        WHERE user_id=?        
    ''', 
    (timezone_id, user_id))
    
    conn.commit()
    conn.close()
    return

def save_reminder(user_id, time_period, time_To, have_first_time_save):
    conn = sqlite3.connect('db/beard_bot_DB.db')
    cursor = conn.cursor()

    if have_first_time_save == 'not yet':
        cursor.execute(
        f'''
            UPDATE users 
            SET reminder_time_{time_period} = ?, first_time_save = ?
            WHERE user_id=?        
        ''', 
        (time_To, time_period, user_id))
    elif have_first_time_save == 'morning/evening':
        cursor.execute(
        f'''
            UPDATE users 
            SET reminder_time_{time_period} = ?, first_time_save = ?
            WHERE user_id=?
        ''', 
        (time_To, "get all", user_id))
    else:
        cursor.execute(
        f'''
            UPDATE users 
            SET reminder_time_{time_period} = ?
            WHERE user_id=?
        ''', 
        (time_To, user_id))
    
    conn.commit()
    conn.close()
    return

def get_user(user_id):
    conn = sqlite3.connect('db/beard_bot_DB.db')
    cursor = conn.cursor()

    cursor.execute('''
        SELECT * FROM users
        JOIN timezones ON timezones.timezone_id = users.timezone_id
        WHERE user_id = ? AND first_time_save == "get all"
    ''', (user_id,))

    user_data = cursor.fetchone()
    conn.close()

    return user_data

def del_time(user_id):
    conn = sqlite3.connect('db/beard_bot_DB.db')
    cursor = conn.cursor()

    cursor.execute(
    f'''
        UPDATE users 
        SET reminder_time_morning = ?, reminder_time_evening = ?
        WHERE user_id=?        
    ''', 
    ('нет', 'нет', user_id))
    
    conn.commit()
    conn.close()
    return

def get_users():
    conn = sqlite3.connect('db/beard_bot_DB.db')
    cursor = conn.cursor()

    cursor.execute('''
        SELECT * FROM users WHERE first_time_save="get all"
    ''')

    user_data = cursor.fetchall()
    conn.close()

    return user_data

def get_all_user_chat_ids():
        conn = sqlite3.connect('db/beard_bot_DB.db')
        cursor = conn.cursor()

        cursor.execute("SELECT user_id FROM users")

        chat_ids = cursor.fetchall()
        conn.close()
        return [chat_id[0] for chat_id in chat_ids]