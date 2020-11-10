from flask import Blueprint
from flask import render_template, url_for

from app.bot.service import send_message

bot_bp = Blueprint('bot_bp', __name__, template_folder='templates', static_folder='static')


@bot_bp.route('/')
def index():
    send_message('kek')
    return render_template('index.html')
