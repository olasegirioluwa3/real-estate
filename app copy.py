from flask import Flask
from config import SECRET_KEY, DB_URI
from flask_sqlalchemy import SQLAlchemy
from models import User, Listing  # Import the models explicitly
from flask_migrate import Migrate

# Initialize the Flask app
app = Flask(__name__)

# Configure the Flask app using values from config.py
app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Create the SQLAlchemy database instance
db = SQLAlchemy(app)
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    is_confirmed = db.Column(db.Boolean, default=False)
    # Add more fields as needed

class Listing(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    price = db.Column(db.Float)
    description = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    # Add more fields as needed


# Initialize Flask-Migrate with the app and db
migrate = Migrate(app, db)

# Import and register the API routes from routes.py
from routes import *

if __name__ == '__main__':
    
    # Run the Flask app
    app.run(debug=True)
