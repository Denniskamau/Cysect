#Third party imports
from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 
from flask_login import LoginManager 
from flask_migrate import Migrate 
from flask_bootstrap import Bootstrap

#local import 
from config import app_config
#db_variable initialization
db = SQLAlchemy()
login_manager = LoginManager()

"""
Create a function that given the correct configuration name,
loads the correct configuration from config.py as well as cofigurations 
from instance/config.py
"""

def create_app(config_name):
    app = Flask(__name__,instance_relative_config=True) #select the relative config environment
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_message = 'You must be login to access this page.'
    login_manager.login_view = 'auth.login'
    #create a migrate object that will allow us to run migrations on the app
    migrate = Migrate(app, db)
    Bootstrap(app)

    from app import models

    """
    Register the blueprints 
    """
    from .admin import admin as admin_blueprint
    app.register_blueprint(admin_blueprint, url_prefix='/admin')

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .home import home as home_blueprint
    app.register_blueprint(home_blueprint)
   

    return app
