import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    DEBUG = False


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'notifier_test.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ENV = os.getenv('ENV')
    DEBUG = True


config_by_name = dict(
    dev=DevelopmentConfig,
)
