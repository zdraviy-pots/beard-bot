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

add_timezones()