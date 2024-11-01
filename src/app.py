from flask import Flask,render_template,request
from markupsafe import escape
import os
import json 



app = Flask(__name__)




@app.route("/")
def hello_world():
   return render_template("index.html",message="Data Passed From Backend")


@app.route("/<name>")
def get_messgae(name):
    return str(os.environ)


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {escape(username)}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {escape(subpath)}'

@app.route(rule="/submit/form",methods=['POST'])
def get_userData():
    data =  request.get_data()
    print(data)
    return data



