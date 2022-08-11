from services.admin_services import admin_login, emailExists, register_admin, usernameExists
from flask import redirect, jsonify, request, session


def index():
    return redirect('/')


def register():
    if request.method == "POST":
        body = request.form.get
        if (body('username') == "" or body('email') == "" or body('password') == ""):
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
        if (body('username') == "" or body('password') == ""):
            msg = "All fields are required"
        else:
            if admin_login(body):
                session['admin'] = 'username'
                return jsonify({'status': 'success'})
            else:
                msg = "Password Incorrect"

    return jsonify({'status': "error", 'message': msg})
