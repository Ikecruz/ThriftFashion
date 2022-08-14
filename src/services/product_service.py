
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
    data = []

    for cat in categories:
        print(cat.name)
        data.append(
            {
                'id': cat.id,
                'name': cat.name
            }
        )

    return categories


def fetchProducts():
    products = Product.query.all()
    data = []

    for prod in products:
        data.append(
            {
                'id': prod.id,
                'name': prod.name,
                'description':prod.description,
                'quantity':prod.qty,
                'category':prod.category.name,
                'price':prod.price,
                'img':prod.img_url,
                'gender': prod.gender
            }
        )

    return data


def getProductLen():
    products = Product.query.all()

    if products is None:
        return 0
    return len(products)

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
        description=body('description'),
        gender=body('gender')
    )
    try:
        Product.insert(product)
        return True
    except Exception as e:
        print(e)
        return False
 
def fetchProductsByCategory(cat_id):
    products = Product.query.filter_by(category_id=cat_id).all()
    data = []

    for prod in products:
        data.append(
            {
                'id': prod.id,
                'name': prod.name,
                'description':prod.description,
                'quantity':prod.qty,
                'category':prod.category.name,
                'price':prod.price,
                'img':prod.img_url,
                'gender': prod.gender,
            }
        )

    return data

def fetchProductsByGender(g):
    print(g)
    products = Product.query.filter_by(gender=g).all()
    data = []

    for prod in products:
        data.append(
            {
                'id': prod.id,
                'name': prod.name,
                'description':prod.description,
                'quantity':prod.qty,
                'category':prod.category.name,
                'price':prod.price,
                'img':prod.img_url,
                'gender': prod.gender,
            }
        )

    return data

def fetchProductsByPriceRange(range):
    if range == "lowest":
        products = Product.query.order_by(Product.price).all()
    else:
        products = Product.query.order_by(Product.price.desc()).all()
    data = []

    for prod in products:
        data.append(
            {
                'id': prod.id,
                'name': prod.name,
                'description':prod.description,
                'quantity':prod.qty,
                'category':prod.category.name,
                'price':prod.price,
                'img':prod.img_url,
                'gender': prod.gender,
            }
        )

    return data

def getLatestProducts():
    products = Product.query.order_by(Product.date_added.desc()).limit(3).all()

    data = []

    for prod in products:
        data.append(
            {
                'id': prod.id,
                'name': prod.name,
                'description':prod.description,
                'quantity':prod.qty,
                'category':prod.category.name,
                'price':prod.price,
                'img':prod.img_url,
                'gender': prod.gender,
            }
        )

    return data

def getProductById(id):
    product = Product.query.get(id)

    if product is None:
        return False

    data = {
        'id': product.id,
        'name': product.name,
        'description':product.description,
        'quantity':product.qty,
        'category':product.category.name,
        'price':product.price,
        'img':product.img_url,
        'gender': product.gender,
    }

    return data
