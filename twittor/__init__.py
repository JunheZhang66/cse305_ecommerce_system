from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from twittor.config import Config

db = SQLAlchemy()
migrate = Migrate()

from twittor.route import index, login

def create_app():
    app = Flask(__name__)
    # app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///:twittor.db"
    # app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:c9m2s2K2@localhost:3306/test"
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config.from_object(Config)
    db.init_app(app)
    migrate.init_app(app,db)
    app.add_url_rule('/','index',index)
    app.add_url_rule('/login','login',login, methods=['GET','POST'])
    return app