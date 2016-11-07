from app import manager
from flask_migrate import MigrateCommand
 
manager.add_command('db', MigrateCommand)
manager.run()