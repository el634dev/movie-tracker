"""Import packages and modules"""
from flask import Blueprint, render_template, redirect, url_for, flash
from app.models import Movie, Director, User
from app.main.forms import MovieForm, DirectorForm

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
    all_users = User.query.all()
    all_directors = Director.query.all()
    return render_template('index.html', 
            all_movies=all_movies, all_directors=all_directors, all_users=all_users)

# -------------------------------------
# Create a new movie
@main.route('/create_movie', methods=['GET', 'POST'])
def create_movie():
    """Create a new movie"""
    # Make an MovieForm instance
    form = MovieForm()

    # If the form was submitted and is valid, create a new Author object
    if form.validate_on_submit():
        new_movie = Movie(
            name=form.name.data,
            year=form.year.data,
            # audience=form.audience.data
        )

        # and save to the database, then flash a success message to the user and
        db.session.add(new_movie)
        db.session.commit()

        # redirect to the homepage
        flash('New movie was created.')
        return redirect(url_for('main.create_movie', movie_id=new_movie.id))
    # Send the form object to the template, and use it to render the form fields
    return render_template('create_movie.html', form=form)

# -------------------------------------
# Create a new director
@main.route('/create_director', methods=['GET', 'POST'])
def create_director():
    """Create a new director"""
    # Make an DirectorForm instance
    form = DirectorForm()

    # If the form was submitted and is valid, create a new Author object
    if form.validate_on_submit():
        new_director = Director(
            name=form.name.data,
            biography=form.biography.data
        )

        # and save to the database, then flash a success message to the user and
        db.session.add(new_director)
        db.session.commit()

        # redirect to the homepage
        flash('New director was created.')
        return redirect(url_for('main.create_director', director_id=new_director.id))
    # Send the form object to the template, and use it to render the form fields
    return render_template('create_director.html', form=form)

# -------------------------------------
# See director details
@main.route('/director/<director_id>', methods=['GET', 'POST'])
def director_detail(director_id):
    """Director detail page"""
    director = Director.query.get(director_id)
    form = DirectorForm(obj=director)

    # If the form was submitted and is valid, update the fields in the 
    if form.validate_on_submit():
        # Movie object and save to the database, then flash a success message to the 
        form.populate_obj(director)

        db.session.commit()
        flash('Updated director sucessfully')
    # user and redirect to the director detail page
    return render_template('director_detail.html', director=director, form=form)

# -------------------------------------
# See movie details
@main.route('/movie/<movie_id>', methods=['GET', 'POST'])
def movie_detail(movie_id):
    """Movie detail page"""
    movie = Movie.query.get(movie_id)
    form = MovieForm(obj=movie)

    # If the form was submitted and is valid, update the fields in the
    if form.validate_on_submit():
        # Movie object and save to the database, then flash a success message to the
        form.populate_obj(movie)

        db.session.commit()
        flash('Updated movie sucessfully')
    # user and redirect to the director detail page
    return render_template('movie_detail.html', movie=movie, form=form)

# -------------------------------------
# See profile
@main.route('/profile/<username>')
def profile(username):
    """Show user's profile"""
    # Make a query for the user with the given username, and send to the template
    user = User.query.filter_by(username=username).first()
    # STRETCH CHALLENGE: Add ability to modify a user's username or favorite movies
    return render_template('profile.html', user=username)

 ----------------------------------
# Favorite movie route
@main.route('/favorite/<movie_id>', methods=['POST'])
@login_required
def favorite_movie(movie_id):
    """Show favorite movies"""
    movie = Movie.query.get(movie_id)
    if movie in current_user.favorite_movies:
        flash('Movie already in favorites.')
    else:
        current_user.favorite_movies.append(movie)
        db.session.add(current_user)
        db.session.commit()

        flash('Movie added to favorites.')
    return redirect(url_for('main.movie_detail', movie_id=movie_id))

# ----------------------------------
# Unfavorite movie route
@main.route('/unfavorite/<movie_id>', methods=['POST'])
@login_required
def unfavorite_movie(movie_id):
    """Unfavorite movie"""
    movie = Movie.query.get(movie_id)
    if movie not in current_user.favorite_movies:
        flash('Movie not in favorites.')
    else:
        current_user.favorite_movies.remove(movie)
        db.session.add(current_user)
        db.session.commit()

        flash('Movie removed from favorites.')
    return redirect(url_for('main.movie_detail', movie_id=movie_id))
