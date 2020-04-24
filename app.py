import json
import uuid
import sqlite3

from flask import Flask
from flask import request, render_template, jsonify, redirect, url_for

from post import Post
from user import User
from locations import Locations

from basic_authentication import (
    get_password_hash,
    verify_password,
    generate_token,
    verify_token,
    require_login
)

app = Flask(__name__)
location_titles = ['Sofia', 'Bansko', 'Shumen', ]
Locations.drop()
for title in location_titles:
    location = Locations(*(None, title))
    location.save()


@app.route("/index.html")
@require_login
def homepage(user):
    return render_template("index.html", posts=Post.all(), user=user)


@app.route("/login.html", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    if request.method == "POST":
        data = json.loads(request.data.decode('ascii'))
        user = User.find_by_email(data['email'])
        if not user:
            values = (
                None,
                data['email'],
                get_password_hash(data['password'])
            )
            user = User(*values)
            user.create()

        if not verify_password(user, data['password']):
            return jsonify({'token': None})

        token = generate_token(user)
        return jsonify({'token': token.decode('ascii')})


@app.route("/create_post", methods=["GET", "POST"])
@require_login
def create_post(user):
    if not user:
        return 403, "Forbiden"

    if request.method == "GET":
        return render_template("post.html", locations=Locations.all(), user=user)
    if request.method == "POST":    
        post_data = request.form
        if post_data == None:
            return "Bad request", 400
        print(post_data)
        values = (None, post_data["title"], post_data["image"], post_data["size"],
                  post_data["price"], post_data["bed_count"], post_data["location_id"], post_data["description"], user.user_id)
        post = Post(*values)
        post.save()
        return redirect(url_for("create_post"))
