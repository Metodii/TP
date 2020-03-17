import json
import uuid

from flask import Flask
from flask import request, render_template, jsonify

from model.ad import Post

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/ads", methods = ["POST"])

#@require_login
#def create_post(user_id):

def create_post():
    post_data = request.get_json(force=True, silent=True)
    if post_data == None:
        return "Bad request", 400
    post = Post(post_data["title"], post_data["location_id"], post_data["price"], post_data["bed_count"], post_data[]"description"])
    post.save()
    return json.dumps(post.to_dict()), 201

