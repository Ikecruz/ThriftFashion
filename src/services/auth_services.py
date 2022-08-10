from random import random
import string

from passlib.hash import sha256_crypt
from database.db import db
from models.user_model import User
from services.email_services import sendEmail

def genToken():
    S = 6 
    ran = ''.join(random.choices(string.digits, k = S))    
    return str(ran)

def emailExists(user_email):
    userEmail = User.query.filter_by(email= user_email ).first()
    if (userEmail is None):
        return False
    return True

def usernameExists(user_name):
    userName = User.query.filter_by(email= user_name ).first()
    if (userName is None):
        return False
    return True

def register_logic(body):
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