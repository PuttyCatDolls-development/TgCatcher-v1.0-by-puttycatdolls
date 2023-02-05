import os

from dotenv import load_dotenv

load_dotenv()

APP_ID = int(os.getenv('APP_ID'))
APP_HASH = str(os.getenv('APP_HASH'))
BOT_TOKEN = str(os.getenv('BOT_TOKEN'))
BOLTALKA_CHAT_ID = int(os.getenv('BOLTALKA_CHAT_ID'))
CHANNEL_FOR_REPORT = int(os.getenv('CHANNEL_FOR_REPORT'))
