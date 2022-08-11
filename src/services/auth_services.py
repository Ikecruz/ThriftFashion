import random
import string
from flask import session
from flask_sqlalchemy import (SessionBase)

from passlib.hash import sha256_crypt
from database.db import db
from models.user_model import User
from services.email_services import sendEmail

def genToken():
    """
    It generates a random string of 6 digits
    :return: A string of 6 random digits
    """
    S = 6 
    ran = ''.join(random.choices(string.digits, k = S))    
    return str(ran)

def emailExists(user_email):
    """
    If the user_email exists in the database, return True, otherwise return False
    
    :param user_email: The email address of the user
    :return: A boolean value.
    """
    userEmail = User.query.filter_by(email= user_email ).first()
    if (userEmail is None):
        return False
    return True


def usernameExists(user_name):
    """
    If the user_name exists in the database, return True, else return False
    
    :param user_name: The username of the user you want to check
    :return: A boolean value
    """
    userName = User.query.filter_by(email= user_name ).first()
    if (userName is None):
        return False
    return True

def verify_logic(user_email,tk):
    """
    If the user exists and the token matches, then update the user's email_verified field to True
    
    :param user_email: The email address of the user who is trying to verify their email address
    :param tk: token
    :return: A boolean value
    """
    user = User.query.filter_by(email=user_email).first()

    if user is None and user.token != tk:
        return False

    try:
        user.email_verified=True
        User.update(user)
        return True
    except Exception as e:
        print(e)
        return False
    
def register_logic(body):
    """
    It takes a body object, generates a token, creates a user object, inserts the user object into the
    database, and sends an email to the user with the token
    
    :param body: The body of the request
    :return: A boolean value
    """
    generatedToken = genToken()

    user = User(
        name=body('name'), 
        password=sha256_crypt.hash(body('password')), 
        email=body('email'), 
        number=body('number'), 
        username=body('username'), 
        token=generatedToken
    )
    
    try:
        User.insert(user)
        msgBody = f"Hello {body('username')}, In order to complete your registration you'll need to verify your email address. Your token is {generatedToken}"
        sendEmail("Verification Token", body('email'), msgBody)
        return True
    except Exception as e :
        print(e)
        return False

def resendToken(user_email):
    generatedToken = genToken()

    user = User.query.filter_by(email=user_email).first()

    if user is None:
        return False
    
    try:
        user.token = generatedToken
        User.update(user)
        msgBody = f"Hello {user.username}, In order to complete your registration you'll need to verify your email address. Your token is {generatedToken}"
        sendEmail("Verification Token", user_email, msgBody)
        return True
    except Exception as e:
        print(e)
        return False

