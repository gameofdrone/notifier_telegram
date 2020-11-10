import os

from telebot import TeleBot
from dotenv import load_dotenv

load_dotenv()
bot = TeleBot(os.environ.get('TELEGRAM_TOKEN'), parse_mode=None)


@bot.message_handler(commands=['start', 'help'])
def send_notify(message):
    bot.reply_to(message, 'Hello, world')


bot.send_message(419302426, 'kek')
