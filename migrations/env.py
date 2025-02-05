from config import DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT
from sqlalchemy import create_engine, pool
from alembic import context

DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

config = context.config
engine = create_engine(DATABASE_URL, poolclass=pool.NullPool)

def run_migrations_online():
    with engine.connect() as connection:
        context.configure(connection=connection, target_metadata=None)
        with context.begin_transaction():
            context.run_migrations()

run_migrations_online()
