import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    DEBUG = False


class DevelopmentConfig(Config):
    ENV = os.getenv('ENV')
    DEBUG = True


config_by_name = dict(
    dev=DevelopmentConfig,
)
