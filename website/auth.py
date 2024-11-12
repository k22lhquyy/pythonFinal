from flask import Blueprint

auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    return 'This is the login page'


@auth.route('/register')
def register():
    return 'This is the register page'


@auth.route('/logout')
def logout():
    return 'You have been logged out'
