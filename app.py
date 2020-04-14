import json
import uuid
import sqlite3

from flask import Flask
from flask import request, render_template, jsonify, redirect, url_for

from post import Post

app = Flask(__name__)



@app.route("/index.html")
def homepage():
    return render_template("index.html")


#@require_login
#def create_post(user_id):

@app.route("/create_post", methods = ["GET", "POST"])

def create_post():
    if request.method == "GET":
        return render_template("post.html")
    if request.method == "POST":
        post_data = request.form
        if post_data == None:
            return "Bad request", 400
        print(post_data) 
        values = (None, post_data["title"], post_data["image"], post_data["size"], 
        post_data["price"], post_data["bed_count"], post_data["location_id"], post_data["description"])  
        post = Post(*values)
        post.save()
        return redirect(url_for("create_post"))

