from app.extensions import db
from flask_login import UserMixin
import enum

# # -------------------
# class FormEnum(enum.Enum):
#     """Helper class to make it easier to use enums with forms."""
#     @classmethod
#     def choices(cls):
#         return [(choice.name, choice) for choice in cls]

#     def __str__(self):
#         return str(self.value)

# -------------------
# Audience
# class Audience(FormEnum):
#     """Audience Model"""
#     CHILDREN = 'Children'
#     YOUNG_ADULT = 'Young Adult'
#     ADULT = 'Adult'
#     ALL = 'All'

#####################
#    Models         #
####################

# Movie Model
class Movie(db.Model):
    """Movie model"""
    id = db.Column(db.Integer, primary_key=True)
    # Name of movie
    name = db.Column(db.String(80), nullable=False)
    year = db.Column(db.Date)

    def __str__(self):
        return f'<Movie: {self.name}>'

    def __repr__(self):
        return f'<Movie: {self.name}>'

# ------------------------
# Director Model
class Director(db.Model):
    """Director model"""
    id = db.Column(db.Integer, primary_key=True)
    # Name of director
    name = db.Column(db.String(80), nullable=False)
    # Director's biography
    biography = db.Column(db.String(200))
    # movies = db.relationship('movies', back_populates='director')

    def __str__(self):
        return f'<Director: {self.name}>'

    def __repr__(self):
        return f'<Director: {self.name}>'

# --------------------------------
# User Model
class User(db.Model, UserMixin):
    """User Model"""
    id = db.Column(db.Integer, primary_key=True)
    # Username
    username = db.Column(db.String(80), nullable=False, unique=True)
    # Password
    password = db.Column(db.String(200), nullable=False)
    # Favorite movies
    favorite_movies = db.relationship(
        'Movie', secondary='user_movie', back_populates='users_who_favorited')

    def __repr__(self):
        return f'<User: {self.username}>'

favorite_movies_table = db.Table('user_movie',
    db.Column('movie_id', db.Integer, db.ForeignKey('movie.id')),
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'))
)
