import os

#Secret key which is used to sign session cookies for protection against cookie data tampering.
SECRET_KEY = os.urandom(32)

# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode, that will refresh the page when changes are made
DEBUG = True

# Connect to the MYSQL database
SQLALCHEMY_DATABASE_URI = 'mysql://root:@localhost/ThriftFashion'

# Turn off the Flask-SQLAlchemy event system and warning
SQLALCHEMY_TRACK_MODIFICATIONS = False

TESTING = False

MAIL_SERVER = "mail.diagnosisabc.com"

MAIL_PORT = 587

MAIL_USERNAME = "admin@diagnosisabc.com"

MAIL_PASSWORD = "admin"

MAIL_USE_TLS = False

MAIL_USE_SSL = False