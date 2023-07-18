import os
# Get the absolute path of the directory where config.py resides
basedir = os.path.abspath(os.path.dirname(__file__))
# Set the path to the migrations repository directory
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'migrations')

# Configuration settings for your real estate API

# Secret key for secure sessions
SECRET_KEY = 'your_secret_key_here'

# MySQL database configuration
DB_USERNAME = 'root'
DB_PASSWORD = 'mysql'
DB_HOST = 'localhost'
DB_PORT = 3306
DB_NAME = 'real_estate'
DB_URI = f'mysql+mysqlconnector://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

# Email settings (if you plan to send confirmation or password reset emails)
EMAIL_HOST = 'your_email_smtp_server'
EMAIL_PORT = 587
EMAIL_USERNAME = 'your_email_username'
EMAIL_PASSWORD = 'your_email_password'

# Other configuration settings as needed
