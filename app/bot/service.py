import os

from telebot import TeleBot

bot = TeleBot(os.getenv('TELEGRAM_TOKEN'))

def send_message(message: str):
    bot.send_message(os.getenv('CHAT_ID'), message)
