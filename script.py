from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy.orm import sessionmaker
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:mysql@localhost/real_estate'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

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
    user_id = db.Column(db.Integer, ForeignKey('user.id'))
    # Add more fields as needed






@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    email = data['email']
    password = data['password']

    # Check if the email is already registered
    if User.query.filter_by(email=email).first():
        return jsonify({'message': 'Email already registered'})

    # Create a new user
    user = User(email=email, password=generate_password_hash(password))
    db.session.add(user)
    db.session.commit()

    # Send confirmation email to the user (you need to implement this part)

    return jsonify({'message': 'User registered successfully'})

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data['email']
    password = data['password']

    # Find the user by email
    user = User.query.filter_by(email=email).first()

    # Check if the user exists and the password is correct
    if user and check_password_hash(user.password, password):
        # Return a token or session for authentication (you need to implement this part)

        return jsonify({'message': 'Login successful'})

    return jsonify({'message': 'Invalid credentials'})

@app.route('/forgot-password', methods=['POST'])
def forgot_password():
    data = request.get_json()
    email = data['email']

    # Find the user by email
    user = User.query.filter_by(email=email).first()

    if user:
        # Send password reset email to the user (you need to implement this part)

        return jsonify({'message': 'Password reset email sent'})

    return jsonify({'message': 'User not found'})

@app.route('/confirm-email/<token>', methods=['GET'])
def confirm_email(token):
    # Verify the token and update the user's is_confirmed flag (you need to implement this part)

    return jsonify({'message': 'Email confirmed'})

@app.route('/dashboard', methods=['GET'])
def dashboard():
    # Authenticate the user using the provided token or session (you need to implement this part)

    # Retrieve the user's listings based on the user_id
    listings = Listing.query.filter_by(user_id=user_id).all()
    
    result = []
    for listing in listings:
        result.append({
            'id': listing.id,
            'title': listing.title,
            'price': listing.price,
            'description': listing.description
            # Add more fields as needed
        })

    return jsonify(result)







@app.route('/listings', methods=['GET'])
def get_listings():
    listings = Listing.query.all()
    result = []
    for listing in listings:
        result.append({
            'id': listing.id,
            'title': listing.title,
            'price': listing.price,
            'description': listing.description
            # Add more fields as needed
        })
    return jsonify(result)


@app.route('/listings', methods=['POST'])
def create_listing():
    data = request.get_json()
    listing = Listing(title=data['title'], price=data['price'], description=data['description'])
    db.session.add(listing)
    db.session.commit()
    return jsonify({'message': 'Listing created successfully'})

@app.route('/listings/<int:listing_id>', methods=['GET'])
def get_listing(listing_id):
    listing = Listing.query.get(listing_id)
    if listing is None:
        return jsonify({'message': 'Listing not found'})
    return jsonify({
        'id': listing.id,
        'title': listing.title,
        'price': listing.price,
        'description': listing.description
        # Add more fields as needed
    })

@app.route('/listings/<int:listing_id>', methods=['PUT'])
def update_listing(listing_id):
    listing = Listing.query.get(listing_id)
    if listing is None:
        return jsonify({'message': 'Listing not found'})
    data = request.get_json()
    listing.title = data['title']
    listing.price = data['price']
    listing.description = data['description']
    # Update more fields as needed
    db.session.commit()
    return jsonify({'message': 'Listing updated successfully'})

@app.route('/listings/<int:listing_id>', methods=['DELETE'])
def delete_listing(listing_id):
    listing = Listing.query.get(listing_id)
    if listing is None:
        return jsonify({'message': 'Listing not found'})
    db.session.delete(listing)
    db.session.commit()
    return jsonify({'message': 'Listing deleted successfully'})



if __name__ == '__main__':
    app.run()
