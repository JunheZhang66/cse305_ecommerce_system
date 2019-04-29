from flask_script import Manager
from twittor import create_app
from flask_migrate import MigrateCommand
app = create_app()
manager = Manager(app)
manager.add_command('db',MigrateCommand)
if __name__ == "__main__":
    manager.run()