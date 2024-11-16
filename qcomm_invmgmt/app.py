from flask import Flask,app,render_template,jsonify
import os


app  =  Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/envs")
def show_envs():
    return str(os.environ)

