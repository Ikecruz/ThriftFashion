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
