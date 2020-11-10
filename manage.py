from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from dotenv import load_dotenv

from app import create_app, db
from app.bot.models import accuracy

load_dotenv()

config_name = 'dev'
app = create_app(config_name=config_name)

app.app_context().push()

manager = Manager(app)

manager.add_command('db', MigrateCommand)


@manager.command
def run():
    return app.run()


if __name__ == "__main__":
    manager.run()
