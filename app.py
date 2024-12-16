from flask import Flask,render_template,request,abort,make_response,jsonify,redirect,url_for
from markupsafe import escape
from qcomm_usermgmt.src.models.user_registration import UserRegistration
from qcomm_usermgmt.src.service.UserService  import UserService
import jwt
from datetime import datetime,timedelta
import os
from msal import ConfidentialClientApplication

app  =  Flask(__name__)


key = os.getenv('JWT_KEY','https://jwt.io/#debugger-io?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c')


client =  ConfidentialClientApplication(client_id="2b809f53-439a-4432-9378-40b14314116e",
        client_credential="fUK8Q~h~ns-oSVzYUaA5FlNLXzZYxKnVpmnwnbXL",
        authority="https://login.microsoftonline.com/d73f6f5b-ef95-47df-92d1-c327390691b0"
    )


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

@app.route("/msal")
def authorize():
    scope_=["User.Read"]
    auth_url = client.get_authorization_request_url(scopes=scope_,redirect_uri=url_for(endpoint="auth_success",_external=True),)
    return redirect(auth_url)

@app.route("/auth_success")
def auth_success():
  code =  request.args['code']
  scope_=["User.Read"]
  auth_token  =  client.acquire_token_by_authorization_code(code=code,scopes=scope_,redirect_uri=url_for(endpoint="auth_success",_external=True))
  return auth_token