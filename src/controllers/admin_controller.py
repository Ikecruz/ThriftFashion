from services.admin_services import admin_login, emailExists, register_admin, usernameExists
from flask import redirect, jsonify, render_template, request, session


def index():
    if 'admin' not in session:
        return redirect('/admin/login')
    return render_template("admin/index.html")


def product():
      if 'admin' not in session:
            return redirect('/admin/login')
      return render_template("admin/add-product.html")
def products():
      if 'admin' not in session:
            return redirect('/admin/login')
      return render_template("admin/products.html")
def register():
    if request.method == "POST":
        body = request.form.get
        if (body('username') is None or body('email') is None or body('password') is None):
            msg = "All fields are required"
        elif usernameExists(body('username')):
            msg = "Username already exist"
        elif emailExists(body('email')):
            msg = "Email already exist"
        else:
            if (register_admin(body)):
                return jsonify({'status': "success"})

    return jsonify({'status': "error", 'message': msg})


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

