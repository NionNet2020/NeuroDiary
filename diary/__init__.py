from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config

# Создание экземпляра базы данных
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = "auth.login"

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Инициализация расширений
    db.init_app(app)
    login_manager.init_app(app)
    
    # Регистрация Blueprint'ов
    from diary.auth import auth_bp
    from diary.routes import diary_bp
    
    app.register_blueprint(auth_bp)
    app.register_blueprint(diary_bp)
    
    return app