from flask import Flask,render_template,request,abort,make_response,jsonify
from markupsafe import escape
from services import DBService, InventoryData
import os
app  =  Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/envs")
def show_envs():
    return str(os.environ)


@app.route("/sampleinput",methods=["GET"])
def input_sample_data():
    inv_svc:InventoryData =  InventoryData()
    inv_svc.initData()
    return render_template("index.html")
