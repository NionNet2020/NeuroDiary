from flask import Flask
from diary.models import db
from diary.routes import main_bp
from diary.auth import auth_bp
from flask_login import LoginManager
from diary.models import User  # Импортируем модель пользователя

app = Flask(__name__)

# Настройки приложения
app.config['SECRET_KEY'] = 'your_secret_key'  # Замени на свой безопасный ключ
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///diary.db'  # Используем SQLite
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Инициализация базы данных
db.init_app(app)

# Инициализация Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login'  # Перенаправление на страницу входа

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))  # Flask-Login ищет пользователя по ID

# Регистрируем блюпринты (модули маршрутов)
app.register_blueprint(main_bp)  # Основные маршруты
app.register_blueprint(auth_bp, url_prefix='/auth')  # Аутентификация

if __name__ == "__main__":
    app.run(debug=True)
