from flask import Flask,render_template,request,abort,make_response,jsonify
from markupsafe import escape
from models.user_registration import UserRegistration
from service.UserService  import UserService


app  =  Flask(__name__)



@app.route("/")
def render_index_page():
    return render_template("index.html")

@app.route("/registration",methods=["GET"])
def render_reg_page():
    return render_template("user_registration.html")


@app.route("/registration",methods=["POST"])
def save_user():
    form  =  request.form.to_dict()
    user_reg =  UserRegistration()
    for item in form.items():
        key  =  item[0]
        val =item[1]
        user_reg.set_form_data(name=key,value=val)
    usr_svc:UserService =  UserService()
    usr_svc.user_registration(user_reg)
    #usr_svc.user_auth(user_reg)
    #usr_svc.user_communication(user_reg)
    #usr_svc.user_pref(user_reg)
    #usr_svc.user_sess(user_reg)
    return "Success"