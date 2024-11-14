from models.user_registration import UserRegistration
from orm.Entity import User, UserCommunications,UserAuth #, UserAuth, UserSession, UserPref
from service.DBService import DBService
from datetime import datetime

class UserService():

    def __init__(self):
        self.db_svc =  DBService()

    def user_registration(self,obj:UserRegistration):
        user =  User(fname=obj.fname,lname=obj.lname,dob=obj.dob)
        user.communications = UserCommunications(communication_type=obj.prefferd_c_type,value=obj.email,
                                                 choosen_to_communicate = obj.enableNotification)

        user_login = obj.fname[:1]+'_'+obj.lname[:1]
        user.user_auth =  UserAuth(login=user_login)
        self.db_svc.persist_obj(user)

    def get_user_by_login(self,login:str):
        return self.db_svc.get_user_by_login(login)
        
