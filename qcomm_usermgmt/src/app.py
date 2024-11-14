from flask import Flask,render_template,request,abort,make_response,jsonify
from markupsafe import escape
from models.user_registration import UserRegistration
from service.UserService  import UserService
import jwt


app  =  Flask(__name__)


key ="https://jwt.io/#debugger-io?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"


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
    return "Success"

@app.route("/user/<login>")
def get_user(login):
    svc =  UserService()
    data =svc.get_user_by_login(login=login)
    user_id = data.UserAuth.user_id
    user_json = {"user_id":str(user_id)}
    print(user_json)
    token =  jwt.encode(payload=user_json,key=key)
    return jsonify(token)