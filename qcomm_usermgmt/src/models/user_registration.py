from datetime import datetime,date
import sys
import json
class UserRegistration():
   
    def __init__(self):
        self.fname:str = None
        self.lname:str = None
        self.mobile:str = None
        self.email:str = None
        self.dob:datetime = None
        self.prefferd_c_type:str = None
        self.enableNotification:bool = False
        self.address_line_1:str = None
        self.address_line_2:str = None
        self.city:str = None
        self.zipcode:str = None
        self.auth_mode:str = None
        self.enable_mfa:bool = None


    def set_form_data(self, name, value):
        if name == "fname":
            self.fname = value
            return
        if name == "lname":
            self.lname =value
            return
        if name == "mobile":
            self.mobile =value
            return
        if name == "email":
            self.email = value
            return
        if name == "dob":
            self.dob = datetime.strptime(value,'%Y-%m-%d')
            return
        if name == "prefferd_c_type":
            self.prefferd_c_type =  value
            return
        if name == "consent":
            self.enableNotification =  bool(value)
            return
        if name == "address_line_1":
            self.address_line_1 = value
            return
        if name == "address_line_2":
            self.address_line_2 =  value
            return
        if name == "city":
            self.city =  value
            return
        if name == "zipcode":
            self.zipcode = value
            return
        if name == "auth_mode":
            self.address_line_2 =  value
            return
        if name == "enable_mfa":
            self.enable_mfa =  value
            return
        else:
            raise Exception(f"No Property found with Name {name}")
        



