from passlib.hash import sha256_crypt
from models.user_model import User

def getUserDetail(key):
    user = User.query.get(key)

    if user is None:
        return False

    data = {
        'username': user.username,
        'email': user.email,
        'name': user.name,
        'number': user.number,
        'status':user.status
    }
    
    return data


def getUsers():
    users = User.query.all()

    if users is None:
        return []
    data = []
    for user in users:
     data.append({
         'id':user.id,
        'username': user.username,
        'email': user.email,
        'name': user.name,
        'number': user.number,
        'status':user.status
    })
    return data


def getUsercount():
    users = User.query.all()

    if users is None:
        return 0

    return len (users)
def updateUserDetail(key, body):
    user = User.query.get(key)

    if user is None:
        return False

    user.number = body('number')
    user.name = body('name')

    try:
        User.update(user)
        return True
    except Exception as e:
        print(e)
        return False

def check_password(key, password):
    user = User.query.get(key)

    if user is None:
        return False

    passvalid = sha256_crypt.verify(password, user.password)
    if (passvalid):
        return True
    else:
        return False


def updatepassword_logic(key, password):
    user = User.query.get(key)

    if user is None:
        return False
    
    user.password = sha256_crypt.hash(password)

    try:
        User.update(user)
        return True
    except Exception as e:
        print(e)
        return False

def blockuser_logic (uid) :     
  user = User.query.get(uid)

  if user is None:
        print ('empty')
        return False
    
  user.status = False

  try:
        User.update(user)
        return True
  except Exception as e:
        print(e)
        return False


def unblockuser_logic(uid):
  user = User.query.get(uid)

  if user is None:
      print('empty')
      return False

  user.status = True

  try:
      User.update(user)
      return True
  except Exception as e:
      print(e)
      return False



    
