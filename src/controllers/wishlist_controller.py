from services.wishlist_services import addToWishes, deleteWish, getAllWishes
from flask import jsonify, request, session


def addToList ():
    if request.method=="POST":
        body=request.form.get
        if (body('pid') is None):
                msg = "All fields are required"
                return jsonify({ 'status': "error", 'message': msg })
        elif  'key' not in session:
            msg = 'Login to continue'
            return jsonify({'status': "error", 'message': msg})
        else :
          if (addToWishes(body('pid'),session['key'])):
            return jsonify({ 'status': "success" })
    return jsonify({ 'status': "error" })  

def deleteFromWish ():
    if request.method=="POST":
        body=request.form.get
        if (body('pid') is None):
                msg = "All fields are required"
                return jsonify({ 'status': "error", 'message': msg })
        elif  'key' not in session:
            msg = 'Login to continue'
            return jsonify({'status': "error", 'message': msg})
        else :
          if (deleteWish(body('pid'),session['key'])):
            return jsonify({ 'status': "success" })
    return jsonify({ 'status': "error" })
def getWish ():
    if request.method=="GET":
        if  'key' not in session:
            msg = 'Login to continue'
            return jsonify({'status': "error", 'message': msg})
    return jsonify({ 'status': "success" ,'data':getAllWishes(session['key'])})
 