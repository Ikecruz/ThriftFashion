from controllers.product_controller import getProducts
from services.cart_services import getAllOrders, getOrders, getTotalMoney, getTotalMoneyToday, getTotalOrders
from services.user_services import getUserDetail, getUsercount, getUsers
from services.product_service import fetchProducts, getCategories, getProductLen
from services.admin_services import admin_login, emailExists, register_admin, usernameExists
from flask import redirect, jsonify, render_template, request, session


def index():
    if 'admin' not in session:
        return redirect('/admin/login')
    userlen = getUsercount() 
    prodlen = getProductLen()  
    ordlen= getTotalOrders ()
    orders = getAllOrders()
    totmon= getTotalMoney ()
    todmon=getTotalMoneyToday()
    return render_template("admin/index.html",ulen=userlen,plen=prodlen,olen=ordlen,orders=orders,money=totmon,todays_money=todmon)


def  orders():
    if 'admin' not in session:
        return redirect('/admin/login')
    orders = getAllOrders ()    
    return render_template("admin/orders.html",orders=orders)


def users():
    if 'admin' not in session:
        return redirect('/admin/login')
    return render_template("admin/users.html",users=getUsers())


def user(id):
    if 'admin' not in session:
        return redirect('/admin/login')
    data = getUserDetail(id)
    orders= getOrders (id)
    return render_template("admin/user.html",user=data,orders=orders)


def product():
    data = []
    for cat in getCategories():
        data.append(
            {
                'id': cat.id,
                'name': cat.name
            }
        )

    if 'admin' not in session:
            return redirect('/admin/login')

    return render_template("admin/add-product.html",categories=data)
def products():
    data = fetchProducts ()
    if 'admin' not in session:
            return redirect('/admin/login')
    return render_template("admin/products.html",products=data)
    
def register():
    if request.method == "POST":
        msg=''
        body = request.form.get
        if (body('username') is None or body('email') is None or body('password') is None):
            msg = "All fields are required"
            return jsonify({'status': "error", 'message': msg})
        elif usernameExists(body('username')):
            msg = "Username already exist"
            return jsonify({'status': "error", 'message': msg})
        elif emailExists(body('email')):
            msg = "Email already exist"
            return jsonify({'status': "error", 'message': msg})
        else:
            if (register_admin(body)):
                return jsonify({'status': "success"})
    return  
   


def login():
    if request.method == "POST":
        body = request.form.get
        if (body('username')is None or body('password') is None):
            msg = "All fields are required"
            return jsonify({'status': "error", 'message': msg})
        elif usernameExists(body('username'))==False:
             msg = "Invalid useername"
             return jsonify({'status': "error", 'message': msg}) 
        else:
            if admin_login(body):
                session['admin'] = body('username')
                return jsonify({'status': 'success'})
            else:
                msg = "Password Incorrect"
                return jsonify({'status': "error", 'message': msg})

    return render_template("admin/sign-in.html")

