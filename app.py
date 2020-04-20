import json
import uuid
import sqlite3

from flask import Flask
from flask import request, render_template, jsonify, redirect, url_for

from post import Post
from user import User
from locations import Locations

from basic_authentication import generate_password_hash, require_login, verify_password 

app = Flask(__name__)
location_titles = ['Sofia', 'Bansko', 'Shumen',]
Locations.drop()
for title in location_titles:
    location = Locations(*(None, title))
    location.save()

@app.route("/index.html")
def homepage():
    return render_template("index.html", posts=Post.all())


@app.route("/create_post", methods = ["GET", "POST"])
@require_login
def create_post(user_id):
    if request.method == "GET":
        return render_template("post.html", locations=Locations.all())
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

