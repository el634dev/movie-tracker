"""Import packages and modules"""
from flask import Blueprint, render_template, redirect, url_for, flash
from app.models import Movie, Director, Genre, User
from app.main.forms import MovieForm, DirectorForm, GenreForm

from app.extensions import db

main = Blueprint("main", __name__)

#####################
#      Routes       #
####################

# Import app and db from events_app package so that we can run app
# from movies_app.extensions import app, bcrypt, db

# ------------------
# Homepage Route
@main.route('/')
def homepage():
    """Homepage"""
    all_movies = Movie.query.all()
    return render_template('index.html', all_movies=all_movies)


@main.route('/create_movie', methods=['GET', 'POST'])
def create_movie():
    """Create a new movie"""
    form = MovieForm()

    # if form was submitted and contained no errors
    if form.validate_on_submit():
        new_movie = Movie(
            name=form.name.data,
            year=form.year_created.data,
            genres=form.genres.data,
        )

        db.session.add(new_movie)
        db.session.commit()

        flash('New movie was created successfully.')
        # Change
        return redirect(url_for('main.movie_detail', movie_id=new_movie.id))
    return render_template('create_movie.html', form=form)


@main.route('/create_director', methods=['GET', 'POST'])
def create_director():
    # TODO: Make an AuthorForm instance

    # TODO: If the form was submitted and is valid, create a new Author object
    # and save to the database, then flash a success message to the user and
    # redirect to the homepage

    # TODO: Send the form object to the template, and use it to render the form
    # fields
    return render_template('create_director.html')


@main.route('/create_genre', methods=['GET', 'POST'])
def create_genre():
    # TODO: Make a GenreForm instance

    # TODO: If the form was submitted and is valid, create a new Genre object
    # and save to the database, then flash a success message to the user and
    # redirect to the homepage

    # TODO: Send the form object to the template, and use it to render the form
    # fields
    return render_template('create_genre.html')


@main.route('/movie/<movie_id>', methods=['GET', 'POST'])
def movie_detail(movie_id):
    movie = Movie.query.get(movie_id)
    form = MovieForm(obj=movie)

    # TODO: If the form was submitted and is valid, update the fields in the 
    # Book object and save to the database, then flash a success message to the 
    # user and redirect to the book detail page
    # Change
    return render_template('movie_detail.html', movie=movie, form=form)


@main.route('/profile/<username>')
def profile(username):
    # TODO: Make a query for the user with the given username, and send to the
    # template

    # STRETCH CHALLENGE: Add ability to modify a user's username or favorite 
    # books
    return render_template('profile.html', username=username)