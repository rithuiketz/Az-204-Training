from flask import Flask,render_template,request,abort,make_response,jsonify
from markupsafe import escape
from services import DBService, InventoryData

app  =  Flask(__name__)

@app.route("/sampleinput",methods=["GET"])
def input_sample_data():
    inv_svc:InventoryData =  InventoryData()
    inv_svc.initData()
    return render_template("index.html")