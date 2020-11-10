from flask import Flask

from config import config_by_name


def create_app(config_name):
    server = Flask(__name__)
    server.config.from_object(config_by_name[config_name])

    register_blueprints(server=server)

    return server

def register_blueprints(server: Flask):
    from app.bot.controler import bot_bp
    server.register_blueprint(bot_bp)
