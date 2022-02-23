# pipenv install Flask-SQLAlchemy Flask-Migrate 
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Product(db.Model):
    __tablename__ = "product"
    
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Text, nullable=False)