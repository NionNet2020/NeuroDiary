from flask import Flask
from flask_login import LoginManager
from .models import db, User

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    # Инициализация базы данных
    db.init_app(app)

    # Инициализация Flask-Login
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = "auth.login"  # Редирект на страницу входа, если не авторизован

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    return app
