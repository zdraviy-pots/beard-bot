import sqlite3

timezones = [
    (2, 'Калининград', '+2'),
    (3, 'Москва', '+3'),
    (4, 'Самара', '+4'),
    (5, 'Екатеринбург', '+5'),
    (6, 'Омск', '+6'),
    (7, 'Красноярск', '+7'),
    (8, 'Иркутск', '+8'),
    (9, 'Якутск', '+9'),
    (10, 'Владивосток', '+10'),
    (11, 'Магадан', '+11'),
    (12, 'Камчатка', '+12'),
]

def create_db():
    conn = sqlite3.connect('db/beard_bot_DB.db')
    cursor = conn.cursor()

    cursor.execute('''           
        CREATE TABLE IF NOT EXISTS timezones (
            timezone_id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            offset_utc TEXT
        )
    ''')

    cursor.execute('''           
        CREATE TABLE IF NOT EXISTS users (
            user_id BIGINT PRIMARY KEY,
            reminder_time_morning TEXT,
            reminder_time_evening TEXT,
            first_time_save TEXT,
            timezone_id INTEGER, 
            FOREIGN KEY (timezone_id) REFERENCES timezones(timezone_id)
        )
    ''')

    conn.commit()
    conn.close()

def add_timezones():
    conn = sqlite3.connect('db/beard_bot_DB.db')
    cursor = conn.cursor()

    cursor.executemany(
        '''
        INSERT INTO timezones (timezone_id, title, offset_utc)
        VALUES (?, ?, ?)
        ''', timezones
    )
    
    conn.commit()
    conn.close()

def save_user(user_id):
    conn = sqlite3.connect('db/beard_bot_DB.db')
    cursor = conn.cursor()

    cursor.execute(
    f'''
        INSERT OR IGNORE INTO users (user_id, first_time_save)
        VALUES (?, "not yet")
    ''', 
    (user_id,))
    
    conn.commit()
    conn.close()
    return

create_db()
add_timezones()