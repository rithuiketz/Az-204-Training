from models.user_registration import UserRegistration
from orm.Entity import User, UserCommunications , UserAuth, UserSession, UserPref
from service.DBService import DBService
from datetime import datetime

class UserService():

    def __init__(self):
        self.db_svc =  DBService()

    def user_registration(self,obj:UserRegistration):
        print(obj.lname)
        user =  User(fname=obj.fname,lname=obj.lname,dob=obj.dob)
        self.db_svc.persist_obj(user)
        
    def user_communication(self,obj:UserRegistration):
        userComm =  UserCommunications(communication_type = obj.prefferd_c_type,value = obj.prefferd_c_type ,chosen_to_communicate = obj.enableNotification)
        self.db_svc.persist_obj(userComm)
        
    def user_pref(self,obj:UserRegistration):
        userPref =  UserPref(pref_type = obj.prefferd_c_type,value = obj.prefferd_c_type)
        self.db_svc.persist_obj(userPref)
    
    def user_auth(self,obj:UserRegistration):
        userAuth =  UserAuth(auth_mode = obj.auth_mode,two_factor_enabled = obj.enable_mfa)
        self.db_svc.persist_obj(userAuth)
        
    def user_sess(self,obj:UserRegistration):
        userSess =  UserSession(start_time = datetime.now())
        self.db_svc.persist_obj(userSess)
    
    
    
    
