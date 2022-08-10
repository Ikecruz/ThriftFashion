import os

#Secret key which is used to sign session cookies for protection against cookie data tampering.
SECRET_KEY = os.urandom(32)

# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode, that will refresh the page when you make changes.
DEBUG = True

# Connect to the MYSQL database
SQLALCHEMY_DATABASE_URI = 'mysql://root:@localhost/ThriftFashion'

# Turn off the Flask-SQLAlchemy event system and warning
SQLALCHEMY_TRACK_MODIFICATIONS = False