from flask import render_template, url_for

def index():
    return render_template("index.html")