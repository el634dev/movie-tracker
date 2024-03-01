from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, ValidationError

# -------------------------
# Movie Form
class MovieForm(FlaskForm):
    """Form to create a movie"""
    name = StringField('Name',
        validators=[DataRequired(), Length(min=3, max=80)])
    year = DateField('Date Created')
    submit = SubmitField('Submit')

# ----------------------------
# Director Form
class DirectorForm(FlaskForm):
    """Form to create a director"""
    # the director's name
    name = StringField('Name',
            validators=[DataRequired(), Length(min=3, max=80)])
    # the director's biography
    biography = TextAreaField('Biography', validators=[DataRequired()])
    # - a submit button
    submit = SubmitField('Submit')

# -------------------------
# User Form
class UserForm(FlaskForm):
    """Form to create genres"""
    # the users name 
    name = StringField('Genre Name', validators=[DataRequired()])
    # - a submit button
    submit = SubmitField('Submit')
