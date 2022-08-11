import datetime
import os
import random
import string
from werkzeug.utils import secure_filename
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])


def allowed_file(filename:str):
    return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS


def getDate():
    x = datetime.datetime.now()
    return x.strftime("%Y-%m-%d")


def genRandomStr():
    S = 30
    ran = ''.join(random.choices(string.ascii_lowercase + string.digits, k=S))
    return str(ran)


def upload_file(image):
        newimgname = f"{getDate()}{genRandomStr()}.png"
        image.filename = newimgname
        filename = secure_filename(image.filename)  
        image.save(os.path.join('static/products', filename))
        return filename



