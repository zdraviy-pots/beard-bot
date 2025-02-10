import sqlite3

def create_db():
    """Создаем базу данных и таблицу, если их нет"""
    conn = sqlite3.connect('db/reminders.db')  # Создаем базу данных (файл)
    cursor = conn.cursor()

    # Создаем таблицу для хранения напоминаний (если таблица не существует)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS reminders (
            user_id INTEGER PRIMARY KEY,
            reminder_time TEXT,
            timezone TEXT
        )
    ''')
    conn.commit()
    conn.close()

create_db()
