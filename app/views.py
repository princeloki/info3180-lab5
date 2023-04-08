"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""

from app import app,db
from flask import render_template, request, jsonify, send_file, url_for, flash, abort,send_from_directory, url_for, jsonify
from flask_wtf.csrf import generate_csrf
import os
from werkzeug.utils import secure_filename
from app.models import MoviesProfile
from app.forms import MovieForm


###
# Routing for your application.
###

@app.route('/')
def index():
    return jsonify(message="This is the beginning of our API")

@app.route('/api/v1/movies', methods=['POST'])
def movies():
    print("Targetted")
    form = MovieForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            title = form.title.data
            description = form.description.data
            poster = form.poster.data
            
            poster_path = secure_filename(poster.filename)
            
            # poster.save(os.path.join(app.config['UPLOAD_FOLDER'], poster_path))
            absolute_dir = os.path.abspath(os.curdir)
            print(absolute_dir)
            poster.save(os.path.join(absolute_dir,app.config['UPLOAD_FOLDER'],poster_path))
            
            moviemodel = MoviesProfile(
                title = title,
                description = description,
                poster = poster_path
            )
            db.session.add(moviemodel)
            db.session.commit()
            flash('Movie saved', 'success')
            return jsonify({
                "message":"Movie Successfully added",
                "title": title,
                "poster": poster_path,
                "description": description
            })
            
        return jsonify({
            "errors": form_errors(form)
        })
        
@app.route('/api/v1/movies', methods=['GET'])
def get_movies():
    movies = MoviesProfile.query.all()
    for movie in movies:
        print(url_for('get_poster', filename=movie.poster))
    n_movies = [{"id":movie.id, "title":movie.title, "description":movie.description, "poster":"uploads\\"+movie.poster} for movie in movies]
    return jsonify({"movies": n_movies})

@app.route('/api/v1/posters/<filename>', methods=['GET'])
def get_poster(filename):
    uploads = app.config['UPLOAD_FOLDER']
    link = os.path.join(uploads+"\\"+filename)
    return link

@app.route('/api/v1/csrf-token', methods=['GET'])
def get_csrf():
    return jsonify({'csrf_token':generate_csrf()})

###
# The functions below should be applicable to all Flask apps.
###

# Here we define a function to collect form errors from Flask-WTF
# which we can later use
def form_errors(form):
    error_messages = []
    """Collects form errors"""
    for field, errors in form.errors.items():
        for error in errors:
            message = u"Error in the %s field - %s" % (
                    getattr(form, field).label.text,
                    error
                )
            error_messages.append(message)

    return error_messages

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404