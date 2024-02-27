from flask_wtf import FlaskForm
from app.extensions import bcrypt
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError
from app.models import User

class SignUpForm(FlaskForm):
    """Sign Up Form"""
    username = StringField('Username', 
            validators=[DataRequired(), Length(min=3, max=50)])
    # Password
    password = PasswordField('Password', 
            validators=[DataRequired(), Length(min=3, max=50)])
    # Submit
    submit = SubmitField('Submit')

    def validate_user(self, username):
        """Validate a user"""
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different username.')

class LoginForm(FlaskForm):
    """Login Form"""
    username = StringField('Username', 
            validators=[DataRequired(), Length(min=3, max=50)])
    # Password
    password = PasswordField('Password', 
            validators=[DataRequired(), Length(min=3, max=50)])
    # Submit
    submit = SubmitField('Submit')

    # -----------------------------------
    # Validate Username
    def validate_username(self, username):
        """Validate a username"""
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different username.')

    # -----------------------------------
    # Validate Password
    def validate_password(self, password):
        """Validate a password"""
        user = User.query.filter_by(username=self.username.data).first()

        if user and not bcrypt.check_password_hash(
            user.password, password.data):
            raise ValidationError('Password does not match. Please try again.')