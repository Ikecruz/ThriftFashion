from sqlalchemy import func
from models.order_model import Order
import re
from models.product_model import Product
from models.cart_model import Cart


def productInCart(body):
    product = Cart.query.filter_by(product_id=body('pid')).first()
    if product is None:
        return False
    return True    

def qtyIsInStock (body):
     product = Product.query.filter_by(id=body('pid')).first()
     if product is None or int(product.qty) < int(body('qty')):
       return False
     return True    
def addProductToCart(body,userId):
    product = Product.query.filter_by(id=body('pid')).first()
    if product is None:
       return False
    cart = Cart (
        product_id=product.id,
        user_id=userId,
        price=int(body('qty')) * product.price,
        quantity=int(body('qty'))
    )
    product.qty -= int(body('qty'))
    
    try:
        Cart.insert(cart)
        Product.update (product)
        return True
    except Exception as e:
        print(e)
        return False


def updateProductInCart(body, userId):
    product = Product.query.filter_by(id=body('pid')).first()
    cart = Cart.query.filter_by(product_id=body('pid'),user_id=userId).first()
    qty = cart.quantity+int(body('qty'))
    price = qty * product.price,
    cart.quantity = qty
    cart.price = price
    product.qty -= int(body('qty'))
    try:
        Cart.update(cart)
        Product.update(product)
        return True
    except Exception as e:
        print(e)
        return False


def deleteProductInCart(body, userId):
    product = Product.query.filter_by(id=body('pid')).first()
    cart = Cart.query.filter_by(product_id=body('pid'), user_id=userId).first()
    qty = cart.quantity
    product.qty += qty
    try:
        Cart.delete(cart)
        Product.update(product)
        return True
    except Exception as e:
        print(e)
        return False


def cartIdExist(cid):
    cart = Cart.query.filter_by(id=cid).first()
    if cart is None:
      return False
    return True  


def cartIdIsNotEmpty(uid):
    cart = Cart.query.filter_by(user_id=uid).all()
    if cart is None:
      return False
    return True
def checkout(uid):
    cart = Cart.query.filter_by(user_id=uid).all()
    # pdlen=len (cart)
    total = Cart.query.with_entities(func.sum(Cart.price).label(
        'sum')).filter_by(user_id=uid).first().sum
    qty = Cart.query.with_entities(
        func.sum(Cart.quantity).label('sum')).filter_by(user_id=uid).first().sum
    order = Order (
        user_id=uid,
        quantity=qty,
        total=total,
    )    
    try:
        Order.insert (order)
        for item in cart :
            Cart.delete(item)
        return True
    except Exception as e:
        print(e)
        return False

def getTotalOrders ():
     orders = Order.query.all()

     if orders is None:
        return 0
     return len(orders)


def getOrders(uid):
    orders = Order.query.filter_by(user_id=uid).all()

    if orders is None:
        return []
    data = []
    for order in orders:
     data.append(
                {
                    'id': order.id,
                    'quantity': order.quantity,
                    'price': order.total,
                    'date': order.date_added,
                    'status':order.status,
                    'user':order.user.name
                }
            )
    return data 


def getAllOrders():
    orders = Order.query.all()

    if orders is None:
        return []
    data = []
    for order in orders:
     data.append(
         {
             'id': order.id,
             'quantity': order.quantity,
             'price': order.total,
             'date': order.date_added,
             'status': order.status,
             'user': order.user.name
         }
     )
    return data
