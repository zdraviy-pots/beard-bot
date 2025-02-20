import sqlite3

def get_first_time_save(user_id):
    conn = sqlite3.connect('db/beard_bot_DB.db')
    cursor = conn.cursor()

    cursor.execute(
    '''
        SELECT first_time_save FROM users WHERE user_id = ?
    ''', 
    (user_id,))

    reminder = cursor.fetchone()
    conn.close()
    return reminder

def get_user_offset(user_id):
    conn = sqlite3.connect('db/beard_bot_DB.db')
    cursor = conn.cursor()

    cursor.execute('''
        SELECT offset_utc FROM timezones
        JOIN users ON users.timezone_id = timezones.timezone_id
        WHERE user_id = ?
    ''', (user_id,))

    offset_utc = cursor.fetchone()[0]
    conn.close()

    return offset_utc