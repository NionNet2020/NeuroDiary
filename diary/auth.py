from flask import render_template, redirect, url_for, flash
from flask_login import login_user, login_required, logout_user
from .models import db, User
from .forms import LoginForm, RegistrationForm
from werkzeug.security import check_password_hash
from flask import Blueprint

auth = Blueprint('auth', __name__)

# Страница регистрации
@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('You have successfully registered!', 'success')
        return redirect(url_for('auth.login'))
    return render_template('register.html', form=form)

# Страница входа
@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            return redirect(url_for('index'))
        flash('Invalid username or password', 'danger')
    return render_template('login.html', form=form)

# Выход из системы
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))
