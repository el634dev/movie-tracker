from flask import Blueprint, request, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user

# from app.auth.forms import SignUpForm, LoginForm
# from app.main.forms import User

# from app.extensions import app, db, bcrypt

auth = Blueprint("auth", __name__)

# -----------------------
# Signup a user
@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    """Sign Up"""
    pass
    # form = SignUpForm()

    # if form.validate_on_submit():
    #     hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
    #     user = User(
    #         username = form.username.data,
    #         password = hashed_password
    #     )

    #     db.session.add(user)
    #     db.session.commit()
    #     flash('Account created.')
    #     return redirect(url_for('auth.login'))
    # return render_template('signup.html', form=form)

# -----------------------
# Login a user
@auth.route('/login', methods=['GET', 'POST'])
def login():
    """Login in a user"""
    pass
    # form = LoginForm()

    # if form.validate_on_submit():
    #     user = User.query.filter_by(username=form.username.data).first()
    #     login_user(user, remember=True)

    #     next_page = request.args.get('next')
    #     return redirect(next_page if next_page else url_for('main.homepage'))
    # return render_template('login.html')

# -----------------------
# Logout a user
@auth.route('/logout')
def logout():
    """logout user"""
    logout_user()
    return redirect(url_for('main.homepage'))
