import json
import uuid
import sqlite3
import uuid
import datetime

from flask import Flask
from flask import request, render_template, jsonify, redirect, url_for

from post import Post
from user import User
from locations import Locations
from werkzeug.utils import secure_filename

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
    return render_template("index.html", user=user)


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

        f = request.files['image']
        filename = secure_filename(str(uuid.uuid1()))
        f.save("static/images/submitted/{}".format(filename))

        values = (None, post_data["title"], filename, post_data["size"], post_data["price"], post_data["bed_count"],
        post_data["location_id"], post_data["available_from"], post_data["available_to"], post_data["description"], user.user_id)
        post = Post(*values)
        post.save()
        return redirect(url_for("create_post"))

@app.route("/view.html")
def view_post():
    return render_template("view.html", posts=Post.all())

@app.route("/post_entries")
def post_entries():
    return render_template("post_entries.html", posts=Post.all(request.args.get('available_from'), request.args.get('available_to')))
