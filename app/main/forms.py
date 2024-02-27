from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, ValidationError
from app.models import Movie, Director, Genre, User


# -------------------------
# Movie Form
class MovieForm(FlaskForm):
    """Form to create a movie"""
    name = StringField('Movie Name',
        validators=[DataRequired(), Length(min=3, max=80)])
    year_created = DateField('Year Created')
    # director = SelectField('Director', allow_blank=False)
    genres = SelectField('Genres')
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
# Genre Form
class GenreForm(FlaskForm):
    """Form to create genres"""
    # the genre's name (e.g. fiction, non-fiction, etc)
    name = StringField('Genre Name', validators=[DataRequired()])
    # - a submit button
    submit = SubmitField('Submit')
