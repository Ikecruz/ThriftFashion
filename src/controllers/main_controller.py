from flask import render_template, session

def index():
    loggedIn = False
    if "key" in session:
        loggedIn = True
    return render_template("index.html", loggedIn=loggedIn)

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