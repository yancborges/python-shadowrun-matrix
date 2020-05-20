from flask import Blueprint, g, redirect, render_template, request, session, \
    url_for, flash
from werkzeug.security import check_password_hash, generate_password_hash
from flaskr.db import get_db
import functools

auth = Blueprint('auth', __name__, url_prefix='/auth')


@auth.route('/register', methods=['GET', 'POST'])
def register():

    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None

        if not username:
            error = 'Username is required.'

        elif not password:
            error = 'Password is required.'

        elif list(db.users.find({'username': username})):
            error = 'User {} is already registered.'.format(username)

        if error is None:
            db.users.insert({
                'username': username,
                'password': generate_password_hash(password)
            })
            return redirect(url_for('auth.login'))

        flash(error)

    return render_template('auth/register.html')


@auth.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None

        user = db.users.find_one({'username': username})
        if not user or not check_password_hash(user['password'], password):
            error = 'Any combination of user and password found.'

        if error is None:
            session.clear()
            session['user_id'] = user['_id']
            return redirect(url_for('index'))

        flash(error)

    return render_template('auth/login.html')


@auth.before_app_request
def load_logged_in_user():

    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = get_db().users.find({'_id': user_id})


@auth.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view
