from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
Gaming = 'database.sqlite3'


def create_database():
    db.create_all()
    print('Database created')


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'abcdefghijklmnopqrstuvwxyzABCDEF'

    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{Gaming}'

    db.init_app(app)

    from .views import views
    from .auth import auth
    from .admin import admin

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(admin, url_prefix='/')

    with app.app_context():
        create_database()

    return app
