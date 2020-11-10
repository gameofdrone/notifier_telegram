from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from config import config_by_name

db = SQLAlchemy()

def create_app(config_name):
    server = Flask(__name__)
    server.config.from_object(config_by_name[config_name])

    db.init_app(server)

    migrate = Migrate(server, db)

    register_blueprints(server=server)

    return server

def register_blueprints(server: Flask):
    from app.bot.controler import bot_bp
    server.register_blueprint(bot_bp)
