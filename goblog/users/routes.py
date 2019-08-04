from flask import Blueprint

users = Blueprint('users', __name__)


@users.route('/register')
def register():
    return "This page will be  used for registering the users"


@users.route('/login')
def login():
    return "This page will be for login"


@users.route('/logout')
def logout():
    return "This page will be for logout"


@users.route('/account')
def account():
    return "This page will be for viewing the account details"


@users.route('/user/<string:username>')
def user_post(username):
    return "This page will be for making a new post"


@users.route('/reset_password')
def reset_request():
    return "This page will be for requesting for resetting password"


@users.route('/reset_password/<token>')
def reset_token(token):
    return "This page is for creating new password"