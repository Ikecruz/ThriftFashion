from models.wishlist_model import WishList
from models.product_model import Product


def addToWishes(pid, uid):
    wishlist = WishList(
        user_id=uid,
        product_id=pid,
    )

    try:
        WishList.insert(wishlist)
        return True
    except Exception as e:
        return False


def getAllWishes (uid):
    wishlist = WishList.query.filter_by(user_id=uid).all()
    if wishlist is None :
        return []
    data=[]  
    for wish in wishlist:
         data.append (
             {
                 'id':wish.id,
                 'name':wish.product.name,
                 'price':wish.product.name,
                 'qty':wish.product.qty,
             }
         ) 
    return data     


def deleteWish(pid, uid):
    wishlist = WishList.query.filter_by(
        user_id=uid,
        product_id=pid,
    ).first()

    try:
        WishList.delete(wishlist)
        return True
    except Exception as e:
        return False
