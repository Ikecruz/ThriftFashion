from services.user_services import check_password, getUserDetail, updateUserDetail, updatepassword_logic
from flask import session, redirect, request, render_template, jsonify

def index():
    if "key" in session:
        return render_template("user/index.html", loggedIn=True)
    return redirect("/auth/login")

def profile():
    if "key" in session:
        key = session["key"]
        
        if request.method == "GET":
            data = getUserDetail(key)
            if (data):
                return render_template("user/details.html", loggedIn=True ,user_profile=data)
            else:
                return redirect("/auth/login")
        
        if request.method == "POST":
            msg = ""

            body = request.form.get
            if body('name') is None and body('number') is None:
                msg = "All fields are required"
                return jsonify({ 'status': "error", 'message': msg })
            
            if updateUserDetail(key, body):
                return jsonify({ 'status': "success"})
            else:
                msg = "An Error occurred"
                return jsonify({ 'status': "error", 'message': msg })
    else:
        return redirect("/auth/login")

def change_password():
    if "key" in session:
        key = session["key"]
        
        if request.method == "GET":
            return render_template('user/change-password.html', loggedIn=True)
        
        if request.method == "POST":
            body = request.form.get

            if body('new_pass') is None and body('old_pass') is None:
                msg = "All fields are required"
                return jsonify({'status': "error",'message': msg })
            
            if not check_password(key, body('old_pass')):
                msg = "Old Password Incorrect"
                return jsonify({'status': "error",'message': msg })
            else:
                if updatepassword_logic(key, body('new_pass')):
                    return jsonify({'status': "success"})
                else:
                    msg = "Update Error"
                    return jsonify({'status': "error",'message': msg })

    else:
        return redirect("/auth/login")

def order():
    if "key" in session:
        key = session["key"]
        
        if request.method == "GET":
            return render_template('user/orders.html', loggedIn=True, data=[])
    else:
        return redirect("/auth/login")
        
def wishlist():
    if "key" in session:
        key = session["key"]
        
        if request.method == "GET":
            return render_template('user/wishlist.html', loggedIn=True, data=[])
    else:
        return redirect("/auth/login")
        

