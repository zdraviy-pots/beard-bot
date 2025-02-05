import asyncpg
from config import DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT

async def create_db_pool():
    return await asyncpg.create_pool(
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )

async def init_db(pool):
    async with pool.acquire() as conn:
        await conn.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                telegram_id BIGINT UNIQUE,
                name TEXT,
                start_date DATE,
                morning_reminder BOOLEAN DEFAULT TRUE,
                evening_reminder BOOLEAN DEFAULT TRUE
            );
        ''')
