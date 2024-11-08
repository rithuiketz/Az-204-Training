from models.user_registration import UserRegistration
from orm.Entity import User
from service.DBService import DBService

class UserService():

    def __init__(self):
        self.db_svc =  DBService()

    def user_registration(self,obj:UserRegistration):
        print(obj.lname)
        user =  User(fname=obj.fname,lname=obj.lname,dob=obj.dob)
        self.db_svc.persist_obj(user)
