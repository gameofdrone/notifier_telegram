from flask_script import Manager
from dotenv import load_dotenv

from app import create_app

load_dotenv()

config_name = 'dev'
app = create_app(config_name=config_name)

app.app_context().push()

manager = Manager(app)


@manager.command
def run():
    return app.run()


if __name__ == "__main__":
    manager.run()
