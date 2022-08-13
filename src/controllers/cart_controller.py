
import re
from services.product_service import productExists
from services.auth_services import getUserId
from services.cart_services import addProductToCart, productInCart, qtyIsInStock, updateProductInCart
from flask import jsonify, request, session


def addToCart ():
    if request.method=="POST":
        body=request.form.get
        if (body("pid") is None or body("qty") is None):
            msg = 'Fill all fields'
            return jsonify({'status': "error",'message':msg})  
        elif productInCart(body):
                msg = 'Product already in cart'
                return jsonify({'status': "error",'msg':msg})
        elif 'user_email' not in session:
            msg='Login to continue'
            return jsonify({'status': "error",'message':msg})  
        elif qtyIsInStock(body) == False:
            msg = 'Quantity not in stock'
            return jsonify({'status': "error", 'message': msg})
        else :
         id=getUserId(session.get('user_email'))
         if addProductToCart(body,id):
                return  jsonify({'status': "success"})
        return  jsonify({'status': "error"})      
    return 'yes'   
def removeFromCart():
     if request.method=="POST":
        body=request.form.get
        if (body("cid") is None):
            msg = 'Fill all fields'
            return jsonify({'status': "error",'message':msg}) 
         