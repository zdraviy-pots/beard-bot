import os
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.getenv("BOT_TOKEN")
DATABASE_URL= os.getenv("DATABASE_URL")
ADMINS = os.getenv("ADMINS")
admins = ADMINS.split(',')