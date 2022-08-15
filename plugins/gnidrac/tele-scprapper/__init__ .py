

""" Bot CC Scrapper """
import os
from gnidrac import *
# this is a constant (not going to change)
API_KEY = os.getenv("API_KEY")
DATABASE_URL = os.getenv("DATABASE_URL")
OWNER_ID = os.getenv("OWNER_ID")
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID_FORWARD = os.getenv("CHAT_ID_FORWARD")
LOG_CHANNEL_ID = os.getenv("LOG_CHANNEL_ID")