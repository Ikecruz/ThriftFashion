from services.cart_services import getCart, getCartTotal
from flask import redirect, render_template, session, request

from services.product_service import fetchProducts, fetchProductsByCategory, fetchProductsByGender, fetchProductsByPriceRange, getCategories

def index():
    products= fetchProducts()
    loggedIn = False
    if "key" in session:
        loggedIn = True
    return render_template("index.html", loggedIn=loggedIn, products=products)

def about():
    loggedIn = False
    if "key" in session:
        loggedIn = True
    return render_template("about_us.html", loggedIn=loggedIn)

def contact():
    loggedIn = False
    if "key" in session:
        loggedIn = True
    return render_template("contact_us.html", loggedIn=loggedIn)

def products():
    products = fetchProducts()
    categories = getCategories()
    selectedCategory = ""
    selectedPriceRange = ""
    selectedGender = ""
    loggedIn = False

    if "key" in session:
        loggedIn = True

    if request.method == 'POST':
        details = request.form.get
        selectedCategory = details('category') 
        selectedGender = details('gender')
        selectedPriceRange = details('price_range')

        if selectedCategory != "" and selectedCategory != "--Select Category--":
            products = fetchProductsByCategory(selectedCategory)
        elif selectedGender != "" and selectedGender != "--Select Gender--":
            products = fetchProductsByGender(selectedGender)
        elif selectedPriceRange != "" and selectedPriceRange != "--Select Price--":
            products = fetchProductsByPriceRange(selectedPriceRange)
        else:
            products = fetchProducts()
    
    return render_template("product.html", loggedIn=loggedIn, products=products, categories=categories, selectedCategory=selectedCategory, selectedGender=selectedGender, selectedPriceRange=selectedPriceRange )



def checkoutpage():
    if 'key' not in session:
        msg = 'Login to continue'
        return redirect('/auth/login')
    id=session['key']    
    cart=getCart(id)
    total=getCartTotal (id)
    return render_template("user/checkout.html",totalprice=total,cartitems=cart)