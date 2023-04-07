# Add any model classes for Flask-SQLAlchemy here
from . import db
from werkzeug.security import generate_password_hash

class MoviesProfile(db.Model):
    
    __tablename__ = 'movies'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    poster = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    
    def __init__(self, id, title, description, poster, created_at):
        self.id = id
        self.title = title
        self.description = description
        self.poster = poster
        self.created_at = created_at
    