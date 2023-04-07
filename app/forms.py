# Add any form classes for Flask-WTF here
from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileRequired
from wtforms import StringField, TextAreaField, FileField
from wtforms.validators import InputRequired

class MovieForm(FlaskForm):
    title = StringField("title", validators=[InputRequired()])
    description = TextAreaField("description", validators=[InputRequired()])
    poster = FileField("poster", validators=[
        FileAllowed(['jpg', 'png'], 'Images only!'),
        FileRequired()
    ])
    