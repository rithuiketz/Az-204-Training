from flask import Flask,render_template,request,abort,make_response,jsonify,Response
from markupsafe import escape
from services import DBService
from services.InventoryData import InventoryData,TemplateGenerator
import requests as re

from msal import PublicClientApplication,ConfidentialClientApplication

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

@app.route("/<path>")
def generic_path(path):
    return render_template(f"{path}.html")

@app.route("/inv/upload",methods=["POST"])
def upload_data():
    data  = request.files['inv_data'].stream.readlines()
    return render_template("upload.html",data=data)

@app.route("/template")
def download_template():
    template_  = TemplateGenerator().writeFile()
    response = Response(template_, content_type="text/csv")
    response.headers["Content-Disposition"] = "attachment; filename=template.csv"
    return response


@app.route("/msal")
def msal_check():
    app =  ConfidentialClientApplication(client_id='2b809f53-439a-4432-9378-40b14314116e',client_credential='fUK8Q~h~ns-oSVzYUaA5FlNLXzZYxKnVpmnwnbXL',
                                         authority="https://login.microsoftonline.com/d73f6f5b-ef95-47df-92d1-c327390691b0"
                                         
                                         )
    result  = app.acquire_token_for_client(scopes=["2b809f53-439a-4432-9378-40b14314116e/.default"])
    #result = app.acquire_token_interactive(scopes=["scope_"])
    return str(result)

