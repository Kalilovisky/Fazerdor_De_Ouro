# pip3 install telethon

import configparser
import json

from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError

def readingConfigs():
# Reading Configs
    config = configparser.ConfigParser()
    config.read("config.ini")

# Setting configuration values
    api_id = config['Telegram']['api_id']
    api_hash = config['Telegram']['api_hash']

    api_hash = str(api_hash)

    phone = config['Telegram']['phone']
    username = config['Telegram']['username']
