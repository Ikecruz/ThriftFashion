from services.product_service import productExists
from services.auth_services import getUserId
from services.cart_services import addProductToCart, cancel, cartIdExist, cartIdIsNotEmpty, checkout, deleteProductInCart, productInCart, qtyIsInStock, updateProductInCart
from flask import jsonify, request, session


def addToCart():
    if request.method == "POST":
        body = request.form.get
        if (body("pid") is None or body("qty") is None):
            msg = 'Fill all fields'
            return jsonify({'status': "error", 'message': msg})
        elif 'key' not in session:
            msg = 'Login to continue'
            return jsonify({'status': "error", 'message': msg})
        elif productInCart(body):
            msg = 'Product already in cart'
            return jsonify({'status': "error", 'message': msg})
        elif qtyIsInStock(body) == False:
            msg = 'Quantity not in stock'
            return jsonify({'status': "error", 'message': msg})
        else:
            id = session['key']
            if addProductToCart(body, id):
                return jsonify({'status': "success"})
        return jsonify({'status': "error"})
    return 'yes'


def cancelOrder():
     if request.method == "POST":
        body = request.form.get
        if (body("oid") is None ):
            msg = 'Fill all fields'
            return jsonify({'status': "error", 'message':msg})
        elif 'key' not in session:
            msg = 'Login to continue'
            return jsonify({'status': "error", 'message': msg})    
        else :
            if cancel(body("oid")):
                return jsonify({'status': "success"})
     return jsonify({'status': "error"})

def removeFromCart():
    if request.method == "POST":
        body = request.form.get
        if (body("cid") is None):
            msg = 'Fill all fields'
            return jsonify({'status': "error", 'message': msg})
        elif 'key' not in session:
            msg = 'Login to continue'
            return jsonify({'status': "error", 'message': msg})
        elif cartIdExist(body("cid")) == False:
            msg = 'Cart Item Does Not Exist'
            return jsonify({'status': "error", 'message': msg})
        else:
            id = session['key']
            if deleteProductInCart(body, id):
                return jsonify({'status': "success"})
            return jsonify({'status': "error"})


def checkOut():
    if request.method == "POST":
        body = request.form.get
        if 'key' not in session:
            msg = 'Login to continue'
            return jsonify({'status': "error", 'message': msg})

        elif cartIdIsNotEmpty(body("cid")) == False:
            msg = 'Cart Is Empty'
            return jsonify({'status': "error", 'message': msg})
        else:
            if checkout(session['key']):
                return jsonify({'status': "success"})
            return jsonify({'status': "error"})
