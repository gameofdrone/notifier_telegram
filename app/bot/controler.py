from flask import Blueprint
from flask import render_template, url_for

# from app.bot.services.accuracy_service import send_message
from app.bot.services.accuracy_service import get_all_accuracy

bot_bp = Blueprint('bot_bp', __name__, template_folder='templates', static_folder='static', url_prefix='/bot')


@bot_bp.route('/')
def index():
    # send_message('kek')
    return render_template('index.html')


@bot_bp.route('/accuracy')
def get_accur():
    data = get_all_accuracy()
    return render_template('accuracy.html', data=data)

import os
import logging

from aiogram import Bot, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.webhook import SendMessage
from aiogram.utils.executor import start_webhook
from dotenv import load_dotenv

load_dotenv()

# webhook settings
WEBHOOK_PATH = "/bot"  # да, тут пусто
WEBHOOK_URL = "http://4ac35da0c91b.ngrok.io"

# webserver settings
WEBAPP_HOST = 'localhost'  # or ip
WEBAPP_PORT = 5000

logging.basicConfig(level=logging.INFO)

bot = Bot(token=os.getenv('TELEGRAM_TOKEN'))
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())

async def on_startup(dp):
    await bot.set_webhook(WEBHOOK_URL)
    # insert code here to run it after start


async def on_shutdown(dp):
    logging.warning('Shutting down..')

    # insert code here to run it before shutdown

    # Remove webhook (not acceptable in some cases)
    await bot.delete_webhook()

    # Close DB connection (if used)
    await dp.storage.close()
    await dp.storage.wait_closed()

    logging.warning('Bye!')

@dp.message_handler(commands=['help'])
async def echo(message: types.Message):
    # Regular request
    # await bot.send_message(message.chat.id, message.text)

    # or reply INTO webhook
    return message.answer('chego hotel?')

start_webhook(
    dispatcher=dp,
    webhook_path=WEBHOOK_PATH,
    on_startup=on_startup,
    on_shutdown=on_shutdown,
    skip_updates=True,
    host=WEBAPP_HOST,
    port=WEBAPP_PORT,
)
