from app.extensions import db
from flask_login import UserMixin

#####################
#    Models         #
####################

# Movie Model
class Movie(db.Model):
    """Movie model"""
    id = db.Column(db.Integer, primary_key=True)
    # Name of movie
    name = db.Column(db.String(80), nullable=False, unique=True)
    # Name of year
    year = db.Column(db.Date)

    # The director 
    director_id = db.Column(db.Integer, db.ForeignKey('director.id'), nullable=False)
    # director = db.relationship('Director', back_populates='movies')

    # The genres, e.g. horror, sci-fi, fantasy
    # genres = db.relationship(
    #     'Genre', secondary='movie_genre', back_populates='movies')

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


# ------------------------
# Genre Model
class Genre(db.Model):
    """Genre model"""
    id = db.Column(db.Integer, primary_key=True)
    # Genre Name
    name = db.Column(db.String(80), nullable=False, unique=True)
    # Movies associated with genre
    # movies = db.relationship(
    #     'Movie', secondary='movie_director')

    def __str__(self):
        return f'<Genre: {self.name}>'

    def __repr__(self):
        return f'<Genre: {self.name}>'


movie_director_table = db.Table('movie_director',
    db.Column('movie_id', db.Integer, db.ForeignKey('movie.id')),
    db.Column('director_id', db.Integer, db.ForeignKey('director.id'))
)

# --------------------------------
# User Model
class User(db.Model, UserMixin):
    """User Model"""
    id = db.Column(db.Integer, primary_key=True)
    # Username
    username = db.Column(db.String(80), nullable=False, unique=True)
    # Password
    password = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f'<User: {self.username}>'
