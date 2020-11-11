from flask import Blueprint
from flask import render_template, url_for

from app.bot.services.accuracy_service import send_message
from app.bot.services.accuracy_service import get_all_accuracy

bot_bp = Blueprint('bot_bp', __name__, template_folder='templates', static_folder='static', url_prefix='/bot')


@bot_bp.route('/')
def index():
    send_message('kek')
    return render_template('index.html')


@bot_bp.route('/accuracy')
def get_accur():
    data = get_all_accuracy()
    return render_template('accuracy.html', data=data)
