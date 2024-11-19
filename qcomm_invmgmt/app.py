from flask import Flask,render_template,request,abort,make_response,jsonify
from markupsafe import escape
from services import DBService
from services.InventoryData import InventoryData
import requests as re

import os
app  =  Flask(__name__)

API_USER_INFO ="http://localhost:8080"


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

@app.route("/inv/<login>")
def get_user_token(login):
    resp = re.get(API_USER_INFO+f"/user/{login}")
    print(resp)
    cookie = resp.cookies['auth-token']
    return str(cookie)

