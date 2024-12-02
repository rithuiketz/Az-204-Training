from flask import Flask,render_template,request,abort,make_response,jsonify,redirect
from markupsafe import escape
from qcomm_usermgmt.src.models.user_registration import UserRegistration
from qcomm_usermgmt.src.service.UserService  import UserService
import jwt
from datetime import datetime,timedelta
import os


app  =  Flask(__name__)


key = os.getenv('JWT_KEY','https://jwt.io/#debugger-io?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c')


@app.route("/")
def render_index_page():
    return render_template("index.html")

@app.route("/registration",methods=["GET"])
def render_reg_page():
    return render_template("user_registration.html")

@app.route("/envs")
def show_envs():
    return str(os.environ)

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
    now = datetime.now()
    user_json = {"user_id":str(user_id),"Created_time":str(now)}
    token =  jwt.encode(payload=user_json,key=key)
    resp  =make_response("Ok",200)
    resp.set_cookie("auth-token",value=token,expires=now+timedelta(minutes=2))
    return resp

@app.route("/loginPage")
def do_login():
    return render_template("login.html")



@app.route("/auth")
def check_user_authentication():
    cookies =  request.cookies
    if "auth-token" in cookies:
        cookie = cookies['auth-token']
        decoded_data =  jwt.decode(cookie,key=key,algorithms=["HS256"])
        return str(decoded_data)
    else:
        return redirect("/loginPage")



@app.errorhandler(401)
def handle_unauthorized(error):
    resp =  make_response(render_template("401.html",401))
    return resp
