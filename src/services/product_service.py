
from models.product_model import Category, Product


def productExists(pname):
    product = Product.query.filter_by(name=pname).first()
    if (product is None):
        return False
    return True

def categoryExists (cname):
    
    category = Category.query.filter_by(name=cname).first()
    print (cname)
    if (category is None):
        return False
    return True

def getCategories():
    categories = Category.query.all()
    return categories


def get_Products():
    products = Product.query.all()
    return products
def add_category (body):
    category = Category(
        name=body('name')
        )
    try:
        Category.insert(category)
        return True
    except Exception as e:
        print(e)
        return False

def update_stock (body):
    product = Product.query.filter_by(name=body('name')).first()
    product.qty = body('qty')
    try:
        Product.update(product)
        return True
    except Exception as e:
        print(e)
        return False
def add_product(body,img):
    category = Category.query.filter_by(name=body('category')).first()
    product = Product (
        name=body('name'),
        category_id=category.id,
        img_url=img,
        price=body('price'),
        qty=int(body('qty')),
        description=body('description')
    )
    try:
        Product.insert(product)
        return True
    except Exception as e:
        print(e)
        return False
 