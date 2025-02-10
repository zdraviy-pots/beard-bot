import sqlite3

def create_db():
    """Создаем базу данных и таблицу, если их нет"""
    conn = sqlite3.connect('db/reminders.db')  # Создаем базу данных (файл)
    cursor = conn.cursor()

    # Создаем таблицу для хранения напоминаний (если таблица не существует)
    cursor.execute('''           
        CREATE TABLE IF NOT EXISTS timezones (
            timezone_id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            offset_utc TEXT
        )
    ''')

    cursor.execute('''           
        CREATE TABLE IF NOT EXISTS reminders (
            user_id INTEGER PRIMARY KEY,
            reminder_time_first TEXT,
            reminder_time_second TEXT,
            timezone_id INTEGER, 
            FOREIGN KEY (timezone_id) REFERENCES timezones(timezone_id)
        )
    ''')

    conn.commit()
    conn.close()

def conn

create_db()
