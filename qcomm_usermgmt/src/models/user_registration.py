from datetime import datetime,date
import sys
class UserRegistration():
    fname:str
    lname:str
    mobile:str
    email:str
    dob:datetime
    prefferd_c_type:str
    enableNotification:bool

    def set_form_data(self, name, value):
        print(f" {name}  {value}")
        if name == "fname":
            self.fname = value
            return
        if name == "lname":
            self.lname == value
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
        if name == "prefferd_c_type":
            self.prefferd_c_type =  bool(value)
            return
        else:
            raise Exception(f"No Property found with Name {name}")

