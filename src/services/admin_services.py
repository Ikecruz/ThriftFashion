from models.admin_model import Admin
from passlib.hash import sha256_crypt


def emailExists(u_email):
    username = Admin.query.filter_by(email=u_email).first()
    if (username is None):
        return False
    return True


def usernameExists(uname):
    username = Admin.query.filter_by(username=uname).first()
    if (username is None):
        return False
    return True


def register_admin(body):
    admin = Admin(
        password=sha256_crypt.hash(body('password')),
        email=body('email'),
        username=body('username'),

    )
    try:
        Admin.insert(admin)
        return True
    except Exception as e:
        print(e)
        return False
def admin_login (body):
    user = Admin.query.filter_by(username=body('username')).first()
    return sha256_crypt.verify(user.password,body ('password'))
