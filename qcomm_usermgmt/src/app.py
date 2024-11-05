from flask import Flask,render_template,request,abort,make_response,jsonify
from markupsafe import escape


app  =  Flask(__name__)

@app.route("/")
def render_index_page():
    return render_template("index.html")

@app.route("/registration",methods=["GET"])
def render_reg_page():
    return render_template("user_registration.html")

