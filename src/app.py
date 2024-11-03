from flask import Flask,render_template,request,abort,make_response,jsonify
from markupsafe import escape
import os
import json 
import requests as re


MICRO_SERVICE_URL ="http://microservice2.default.svc.cluster.local:8080"



app = Flask(__name__)




@app.route("/")
def hello_world():
   return render_template("index.html",message="Data Passed From Backend")


@app.route("/<name>")
def get_messgae(name):
    return str(os.environ)

@app.route("/microservice/test")
def sampleMS():
    resp =  re.get(MICRO_SERVICE_URL+"/dns/checkDNS")
    body =  jsonify(resp.json())
    return body

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
    for data in request.form.items():
        print(data)
    return "ddd"

@app.route("/400",)
def send_400():
    abort(400)

@app.errorhandler(400)
def handle_400(eror):
    resp = make_response(render_template('400.html'), 404)
    resp.headers['X-Something'] = 'A value'
    return resp


